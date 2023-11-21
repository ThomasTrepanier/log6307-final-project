
import json
import os
from model import Code, Conversation, get_file_name, get_json_value_of_dict, string_not_in_english


class ConversationExtractor:

    def extract_conversations_by_url(self, path: str, print_process: bool = True) -> dict[str, Conversation]:
        conversations_by_url = {}

        with open(path, "r") as file:
            sources = json.load(file)["Sources"]

            for source in sources:
                sharings_json = source["ChatgptSharing"]

                for sharing_json in sharings_json:
                    sharing_url = sharing_json["URL"]
                    status = int(sharing_json["Status"])
                    if (sharing_url in conversations_by_url):
                        if (print_process):
                            print(f"Skipping {
                                  sharing_url}, already in dict...")
                        continue

                    if (status != 200):
                        if (print_process):
                            print(f"Skipping {
                                  sharing_url}, status is {status}...")
                        continue

                    if (print_process):
                        print(f"Extracting {sharing_url}...")

                    conversations = []
                    conversations_json = sharing_json["Conversations"]

                    for conversation_json in conversations_json:
                        prompt = conversation_json[Conversation.PROMPT_KEY]
                        answer = conversation_json[Conversation.ANSWER_KEY]
                        if string_not_in_english(prompt) or string_not_in_english(answer):
                            continue
                        list_of_codes = []

                        for code_json in conversation_json[Conversation.LIST_OF_CODE_KEY]:
                            id = code_json[Code.ID_KEY]
                            type = code_json[Code.TYPE_KEY]
                            content = code_json[Code.CONTENT_KEY]
                            if (string_not_in_english(content)):
                                continue
                            list_of_codes.append(Code(id, type, content))

                        conversations.append(Conversation(
                            prompt, answer, list_of_codes))

                    conversations_by_url[sharing_url] = conversations

        return conversations_by_url

    def save_conversations(self, path: str, conversations_by_url: dict[str, Conversation]):
        file_name = get_file_name(path)
        save_dir = "../data/interim/conversations"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        save_path = f"../data/interim/conversations/{file_name}.json"

        value = get_json_value_of_dict(conversations_by_url)
        with open(save_path, "w") as file:
            json.dump(value, file, default=str)

    def is_csv_file(self, file: str):
        return file.split('.')[-1] == 'csv'

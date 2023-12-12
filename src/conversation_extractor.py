
import json
from conversation_io import ConversationIO
from model import Code, Conversation, get_file_name, string_not_in_english


class ConversationExtractor:

    def __init__(self):
        self.io = ConversationIO()

    def extract_conversations_by_url(self, path: str, print_process: bool = True) -> 'dict[str, Conversation]':
        conversations_by_url = {}

        with open(path, "r") as file:
            sources = json.load(file)["Sources"]

            for source in sources:
                sharings_json = source["ChatgptSharing"]

                for sharing_json in sharings_json:
                    sharing_url = sharing_json["URL"]
                    status = int(sharing_json["Status"])

                    if (print_process):
                        print(f"Extracting {sharing_url}...")

                    if (sharing_url in conversations_by_url):
                        if (print_process):
                            print(f"Skipping, already in dict...")
                        continue

                    if (status != 200):
                        if (print_process):
                            print(f"Skipping, status is {status}...")
                        continue

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

    def save_conversations(self, path: str, conversations_by_url: 'dict[str, Conversation]'):
        save_dir = "../data/interim/conversations"
        file_name = get_file_name(path)

        self.io.save_conversations(save_dir, file_name, conversations_by_url)

    def is_csv_file(self, file: str):
        return file.split('.')[-1] == 'csv'

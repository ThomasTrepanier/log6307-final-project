
import json
import os


class Code:
    ID_KEY = "ReplaceString"
    TYPE_KEY = "Type"
    CONTENT_KEY = "Content"

    def __init__(self, id: str, type: str, content: str):
        self.id = id
        self.type = type
        self.content = content

    # Write a method that makes Code JSON serializable
    def to_json(self):
        return {
            self.ID_KEY: self.id,
            self.TYPE_KEY: self.type,
            self.CONTENT_KEY: self.content
        }


class Conversation:
    PROMPT_KEY = "Prompt"
    ANSWER_KEY = "Answer"
    LIST_OF_CODE_KEY = "ListOfCode"

    def __init__(self, prompt: str, answer: str, list_of_codes: list[Code]):
        self.prompt = prompt
        self.answer = answer
        self.list_of_codes = list_of_codes

    # Write a method that makes Conversation JSON serializable
    def to_json(self):
        return {
            self.PROMPT_KEY: self.prompt,
            self.ANSWER_KEY: self.answer,
            self.LIST_OF_CODE_KEY: [code.to_json()
                                    for code in self.list_of_codes]
        }


class ConversationExtractor:

    def extract(self):
        for subdir, dirs, files in os.walk(f"../data/raw"):
            for file in files:
                if (self.__is_csv_file(file)):
                    continue

                path = os.path.join(subdir, file)
                print(f"Extracting conversations from {path}...")
                conversations_by_url = self.__extract_conversations_by_url(
                    path, print_process=False)
                self.__save_conversations(path, conversations_by_url)

    def __extract_conversations_by_url(self, path: str, print_process: bool = True) -> dict[str, Conversation]:
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
                        list_of_codes = []

                        for code_json in conversation_json[Conversation.LIST_OF_CODE_KEY]:
                            id = code_json[Code.ID_KEY]
                            type = code_json[Code.TYPE_KEY]
                            content = code_json[Code.CONTENT_KEY]
                            list_of_codes.append(Code(id, type, content))

                        conversations.append(Conversation(
                            prompt, answer, list_of_codes))

                    conversations_by_url[sharing_url] = conversations

        return conversations_by_url

    def __save_conversations(self, path: str, conversations_by_url: dict[str, Conversation]):
        file_name = self.get_file_name(path)
        save_path = f"../data/interim/conversations/{file_name}.json"

        value = dict(map(lambda item: (item[0], [conversation.to_json(
        ) for conversation in item[1]]), conversations_by_url.items()))
        with open(save_path, "w") as file:
            json.dump(value, file, default=str)

    def get_file_name(self, path: str):
        last_slash_index = path.rfind('\\')

        # Find the index of the last occurrence of '.'
        last_dot_index = path.rfind('.')

        # Extract the desired substring between the last '/' and '.'
        if last_slash_index != -1 and last_dot_index != -1 and last_slash_index < last_dot_index:
            extracted_substring = path[last_slash_index + 1:last_dot_index]

        return extracted_substring

    def __is_csv_file(self, file: str):
        return file.split('.')[-1] == 'csv'

    @staticmethod
    def get_conversations_from_source(source):
        return source["ChatgptSharing"]

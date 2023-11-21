
import json
import os
from model import Code, Conversation, get_file_name, get_json_value_of_dict


class ConversationFilter:
    def load_conversations(self, path: str) -> dict[str, list[Conversation]]:
        conversations_by_url = {}
        with open(path, "r") as file:
            data = json.load(file)

            for url, conversations_json in data.items():
                conversations = []
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
                conversations_by_url[url] = conversations

        return conversations_by_url

    def get_conversations_with_code(self, conversations_by_url: dict[str, list[Conversation]], print_process: bool = True) -> dict[str, list[Conversation]]:
        if (print_process):
            print("Filtering conversations without code...")
        filtered_conversations = dict(list(map(lambda item: (
            item[0], self.__filter_conversations_without_code(item[1])), conversations_by_url.items())))

        return filtered_conversations

    def get_python_conversations(self, conversations_by_url: dict[str, list[Conversation]], print_process: bool = True) -> dict[str, list[Conversation]]:
        if (print_process):
            print("Filtering python conversations...")
        filtered_conversations = {}

        for url, conversations in conversations_by_url.items():
            for conversation in conversations:
                python_codes = conversation.get_code_of_type("python")
                if (len(python_codes) > 0):
                    if (url not in filtered_conversations):
                        filtered_conversations[url] = []
                    filtered_conversations[url].append(Conversation(
                        conversation.prompt, conversation.answer, python_codes))

        return filtered_conversations

    def get_js_conversations(self, conversations_by_url: dict[str, list[Conversation]], print_process: bool = True) -> dict[str, list[Conversation]]:
        if (print_process):
            print("Filtering js conversations...")
        filtered_conversations = {}

        for url, conversations in conversations_by_url.items():
            for conversation in conversations:
                js_codes = conversation.get_code_of_type("javascript")
                if (len(js_codes) > 0):
                    if (url not in filtered_conversations):
                        filtered_conversations[url] = []
                    filtered_conversations[url].append(Conversation(
                        conversation.prompt, conversation.answer, js_codes))

        return filtered_conversations

    def get_ts_conversations(self, conversations_by_url: dict[str, list[Conversation]], print_process: bool = True) -> dict[str, list[Conversation]]:
        if (print_process):
            print("Filtering ts conversations...")
        filtered_conversations = {}

        for url, conversations in conversations_by_url.items():
            for conversation in conversations:
                ts_codes = conversation.get_code_of_type("typescript")
                if (len(ts_codes) > 0):
                    if (url not in filtered_conversations):
                        filtered_conversations[url] = []
                    filtered_conversations[url].append(Conversation(
                        conversation.prompt, conversation.answer, ts_codes))

        return filtered_conversations

    def get_java_conversations(self, conversations_by_url: dict[str, list[Conversation]], print_process: bool = True) -> dict[str, list[Conversation]]:
        if (print_process):
            print("Filtering java conversations...")
        filtered_conversations = {}

        for url, conversations in conversations_by_url.items():
            for conversation in conversations:
                java_codes = conversation.get_code_of_type("java")
                if (len(java_codes) > 0):
                    if (url not in filtered_conversations):
                        filtered_conversations[url] = []
                    filtered_conversations[url].append(Conversation(
                        conversation.prompt, conversation.answer, java_codes))

        return filtered_conversations

    def __filter_conversations_without_code(self, conversations: list[Conversation]) -> list[Conversation]:
        return list(filter(lambda conversation: conversation.has_code(), conversations))

    def save_conversations(self, conversations_by_url: dict[str, list[Conversation]], type: str):
        save_dir = f"../data/interim/filtered-conversations"

        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        save_path = f"{save_dir}/conversations-{type}.json"

        value = get_json_value_of_dict(conversations_by_url)
        with open(save_path, "w") as file:
            json.dump(value, file, default=str)

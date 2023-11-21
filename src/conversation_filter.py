
import json

from model import Code, Conversation, get_file_name, get_json_value_of_dict


class ConversationFilter:

    def filter_conversations_without_code(self, path: str, print_process: bool = True):
        conversations_by_url = self.__load_conversations(path)
        conversations_by_url = self.__filter_conversations_without_code(
            conversations_by_url, print_process)
        self.__save_conversations(conversations_by_url, path)

    def __load_conversations(self, path: str) -> dict[str, list[Conversation]]:
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

    def __filter_conversations_without_code(self, conversations_by_url: dict[str, list[Conversation]], print_process: bool = True) -> dict[str, list[Conversation]]:
        if (print_process):
            print("Filtering conversations without code...")
        filtered_conversations = dict(list(map(lambda item: (
            item[0], self.__filter_conversations(item[1])), conversations_by_url.items())))

        return filtered_conversations

    def __filter_conversations(self, conversations: list[Conversation]) -> list[Conversation]:
        return list(filter(lambda conversation: conversation.has_code(), conversations))

    def __save_conversations(self, conversations_by_url: dict[str, list[Conversation]], path: str):
        file_name = get_file_name(path)
        save_path = f"../data/interim/conversations-with-code/{file_name}.json"

        value = get_json_value_of_dict(conversations_by_url)
        with open(save_path, "w") as file:
            json.dump(value, file, default=str)

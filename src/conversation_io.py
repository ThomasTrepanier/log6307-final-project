import json
import os
from model import Code, Conversation


class ConversationIO:
    def load_conversations(self, path: str) -> 'dict[str, list[Conversation]]':
        conversations = {}
        with open(path, "r") as file:
            data = json.load(file)
            for url, conversations_json in data.items():
                conversations[url] = []
                for conversation_json in conversations_json:
                    prompt = conversation_json[Conversation.PROMPT_KEY]
                    answer = conversation_json[Conversation.ANSWER_KEY]
                    list_of_codes = []
                    for code_json in conversation_json[Conversation.LIST_OF_CODE_KEY]:
                        id = code_json[Code.ID_KEY]
                        type = code_json[Code.TYPE_KEY]
                        content = code_json[Code.CONTENT_KEY]
                        list_of_codes.append(Code(id, type, content))
                    conversations[url].append(Conversation(
                        prompt, answer, list_of_codes))

        return conversations

    def save_conversations(self, save_dir, file_name, value: 'dict[str, list[Conversation]]'):
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        save_path = f"{save_dir}/{file_name}.json"

        json_value = self.__get_json_value_of_dict(value)
        with open(save_path, "w") as file:
            json.dump(json_value, file, default=str)

    def __get_json_value_of_dict(self, conversations_by_url: 'dict[str, list[Conversation]]'):
        return dict(map(lambda item: (item[0], [conversation.to_json(
        ) for conversation in item[1]]), conversations_by_url.items()))

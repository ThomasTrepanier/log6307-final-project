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

    def __init__(self, prompt: str, answer: str, list_of_codes: 'list[Code]'):
        self.prompt = prompt
        self.answer = answer
        self.list_of_codes = list_of_codes

    def has_code(self) -> bool:
        return len(self.list_of_codes) > 0

    def get_code_of_type(self, type: str) -> 'list[Code]':
        return list(filter(lambda code: code.type == type, self.list_of_codes))

    # Write a method that makes Conversation JSON serializable
    def to_json(self):
        return {
            self.PROMPT_KEY: self.prompt,
            self.ANSWER_KEY: self.answer,
            self.LIST_OF_CODE_KEY: [code.to_json()
                                    for code in self.list_of_codes]
        }


def get_file_name(path: str):
    last_slash_index = path.rfind('\\')

    # Find the index of the last occurrence of '.'
    last_dot_index = path.rfind('.')

    # Extract the desired substring between the last '/' and '.'
    if last_slash_index != -1 and last_dot_index != -1 and last_slash_index < last_dot_index:
        extracted_substring = path[last_slash_index + 1:last_dot_index]

    return extracted_substring


def string_not_in_english(string: str) -> bool:
    return not string.isascii()

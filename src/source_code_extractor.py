from model import Conversation
import os

class SourceCodeExtractor:
    def extract(self, conversations_by_url: 'dict[str, list[Conversation]]'):
        source_codes = []

        for conversations in conversations_by_url.values():
            for conversation in conversations:
                for code in conversation.list_of_codes:
                    if (self.__is_valid_source_code(code.content, type=code.type)):
                        source_codes.append(code.content)

        return source_codes

    
    def export_source_code(self, source_codes, type):
        save_dir = f"../data/interim/src/{type}"

        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        else:
            for file in os.listdir(save_dir):
                os.remove(f"{save_dir}/{file}")

        for i, source_code in enumerate(source_codes):
            save_path = f"{save_dir}/{i}.{self.__get_extension_by_type(type)}"
            with open(save_path, "w") as file:
                file.write(source_code)

    def __is_valid_source_code(self, source_code: str, type):
        if (type == "python"):
            return source_code.find("def") != -1 or source_code.find("class") != -1
        elif (type == "javascript"):
            return source_code.startswith("function")
        elif (type == "typescript"):
            return source_code.startswith("function")
        elif (type == "java"):
            return source_code.startswith("public class")
        else:
            raise Exception(f"Type {type} is not supported")
    
    @staticmethod
    def __get_extension_by_type(type):
        if (type == "python"):
            return "py"
        elif (type == "javascript"):
            return "js"
        elif (type == "typescript"):
            return "ts"
        elif (type == "java"):
            return "java"
        else:
            raise Exception(f"Type {type} is not supported")
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

    def filter_valid_source_code(self, source_codes, type):
        return [source_code for source_code in source_codes if self.__is_valid_source_code(source_code, type)]
    
    def export_source_code(self, origin, source_codes, type, file_index):
        save_dir = f"../data/interim/{origin}/src/{type}"

        print(f"Exporting {len(source_codes)} source codes to {save_dir}")

        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        for i, source_code in enumerate(source_codes):
            save_path = f"{save_dir}/{file_index}_{i}.{self.__get_extension_by_type(type)}"
            with open(save_path, "w") as file:
                file.write(source_code)



    def delete_invalid_files(self, origin, type):
        folder_path = f"../data/interim/{origin}/src/{type}"
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if filename.endswith('.py') and not self.__is_valid_python_file(file_path):
                # print(f"Deleting {filename}")
                os.remove(file_path)

    def __is_valid_source_code(self, source_code: str, type):
        if (type == "python"):
            return (source_code.find("def ") != -1 or source_code.find("class ") != -1) and len(source_code.split("\n")) > 5
        elif (type == "javascript"):
            return source_code.startswith("function")
        elif (type == "typescript"):
            return source_code.startswith("function")
        elif (type == "java"):
            return source_code.startswith("public class")
        else:
            raise Exception(f"Type {type} is not supported")
        
    def __is_valid_python_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                compile(file.read(), file_path, 'exec')
            return True
        except (SyntaxError, TypeError):
            return False
        
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
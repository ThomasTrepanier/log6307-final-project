import os
import json

def read_json_files_in_directory(directory_path):
    data_array = []
    if not os.path.exists(directory_path):
        print(f"The directory '{directory_path}' does not exist.")
        return data_array

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and filename.endswith(".json"):
            try:
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    data_array.append(data)
            except Exception as e:
                print(f"Error reading {file_path}: {str(e)}")

    return data_array

import os
import json

def read_json_files_in_directory(directory_path):
    data_array = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            data_array.append(data)
    return data_array

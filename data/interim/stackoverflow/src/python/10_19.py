import os
from os.path import isfile, join, isdir

def get_files_path(directory, paths):
    for item in os.listdir(directory):
        if isfile(join(directory, item)) and item == "tv.sas7bda":
            paths.append(directory + item)
        elif isdir(directory+item):
            get_files_path(directory + item, paths)
    return paths

directory_to_search = "./"
get_files_path(directory_to_search , [])

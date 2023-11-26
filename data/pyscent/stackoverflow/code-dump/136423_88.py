import os 

def compare_common_files_by_size(directory_one, directory_two):
  d1_files = set(os.listdir(directory_one))
  d2_files = set(os.listdir(directory_two))
  common_files = list(d1_files &  d2_files)
  if common_files:
    for filename in common_files:
       file_01 = os.stat(f'{directory_one}/{filename}')
       file_02 = os.stat(f'{directory_two}/{filename}')
       if file_01.st_size == file_02.st_size:
            print(f'The file - {filename} is identical in the directories {directory_one} and {directory_two}')
       elif file_01.st_size != file_02.st_size:
            print(f'The file - {filename} is different in the directories {directory_one} and'
                  f' {directory_two}')

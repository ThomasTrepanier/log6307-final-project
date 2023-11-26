import filecmp

def compare_common_files(directory_one, directory_two):
  d1_files = set(os.listdir(directory_one))
  d2_files = set(os.listdir(directory_two))
  common_files = list(d1_files & d2_files)
  if common_files:
    for filename in common_files:
        file_01 = f'{directory_one}/{filename}'
        file_02 = f'{directory_two}/{filename}'
        comparison = filecmp.cmp(file_01, file_02, shallow=False)
        if comparison:
            print(f'The file - {filename} is identical in the directories - {directory_one} and {directory_two}')
        elif not comparison:
            print(f'The file - {filename} is different in the directories - {directory_one} and {directory_two}')

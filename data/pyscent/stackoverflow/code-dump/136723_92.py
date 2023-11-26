import filecmp

def directory_recursive(directory_one, directory_two):
   files = filecmp.dircmp(directory_one, directory_two)
   for filename in files.diff_files:
      print(f'The file - {filename} is different in the directories - {files.left} and {files.right}')
   for filename in files.left_only:
      print(f'The file - {filename} - was only found in the directory {files.left}')
   for filename in files.right_only:
      print(f'The file - {filename} - was only found in the directory {files.right}')

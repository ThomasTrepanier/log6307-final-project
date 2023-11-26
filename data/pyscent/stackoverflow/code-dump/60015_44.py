import os
import sys

def rename_first_file_in_dir(dir_path, new_file_name, keep_extension = False):
  for current_file_name in os.listdir(dir_path):
    current_file_path = os.path.join(dir_path, current_file_name) # full or relative path to the file in dir
    if not os.path.isfile(current_file_path):
      break
    # rename only base name of file to the name of directory
    if keep_extension:
      file_extension = os.path.splitext(current_file_name)[1]
      if len(file_extension) > 0:
        new_file_name = new_file_name + file_extension 
        
    new_file_path = os.path.join(dir_path, new_file_name)
    print("File " + current_file_name + " renamed to " + new_file_name + " in " + os.path.basename(dir_path) + " directory");
    os.rename(current_file_path, new_file_path)
    # exit after first processed file
    break

if len(sys.argv) < 2:
  print("Usage: python " + os.path.basename(__file__) + " <directory> [keep_files_extensions]") # help for usage
  exit(0)
scan_dir = sys.argv[1]
keep_extension = False if len(sys.argv) < 3 else not (int(sys.argv[2]) == 0) # optional parameter 0 - False, 1 - True, by default - False
if not os.path.exists(scan_dir):
  print("Error: directory " + scan_dir + " does not exists")
  exit(-1)
if not os.path.isdir(scan_dir):
  print("Error: file " + scan_dir + " is not a directory")
  exit(-1)
print("Scanning directory " + scan_dir)
for file_name in os.listdir(scan_dir): # walk through directory
  file_path = os.path.join(scan_dir, file_name)
  if os.path.isdir(file_path):
    rename_first_file_in_dir(file_path, file_name, keep_extension)

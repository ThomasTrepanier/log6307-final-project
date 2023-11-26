import hashlib

def compare_common_files_by_hash(directory_one, directory_two):
   d1_files = set(os.listdir(directory_one))
   d2_files = set(os.listdir(directory_two))
   common_files = list(d1_files &  d2_files)
   if common_files:
     for filename in common_files:
        hash_01 = hashlib.sha256(open(f'{directory_one}/{filename}', 'rb').read()).hexdigest()
        hash_02 = hashlib.sha256(open(f'{directory_two}/{filename}', 'rb').read()).hexdigest()
        if hash_01 == hash_02:
            print(f'The file - {filename} is identical in the directories {directory_one} and {directory_two}')
        elif hash_01 != hash_02:
            print(f'The file - {filename} is different in the directories {directory_one} and {directory_two}')

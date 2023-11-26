import fs
import os
import boto3
import filecmp

def create_temp_memory_filesystem():
   mem_fs = fs.open_fs('mem://')
   virtual_disk = mem_fs.makedir('hidden_dir')
   return mem_fs, virtual_disk

def query_s3_file_by_name(filename, memory_filesystem, temp_directory):
   s3 = boto3.resource('s3', aws_access_key_id='your_access_key_id',
                    aws_secret_access_key='your_secret_access_key')
   bucket = s3.Bucket('your_bucket_name')
   for obj in bucket.objects.all():
      if obj.key == filename:
        body = obj.get()['Body'].read()
        with memory_filesystem.open(f'{temp_directory}/s3_{filename}', 'w') as f:
            f.write(str(body))
            f.close()

def compare_local_files_to_s3_files(local_csv_files):
   virtual_disk = create_temp_memory_filesystem()
   directory_name = str(virtual_disk[1]).split('/')[1]
   files = set(os.listdir(local_csv_files))
   for filename in files:
      if filename.endswith('.csv'):
        local_file = f'{local_csv_files}/{filename}'
        query_s3_file_by_name(filename, virtual_disk[0], directory_name)
        virtual_files = virtual_disk[0].opendir(directory_name)
        for file_name in virtual_files.listdir('/'):
            comparison = filecmp.cmp(local_file, file_name, shallow=False)
            if comparison:
                print(f'The file - {filename} is identical in both the local file system and the S3 bucket.')
            elif not comparison:
                print(f'The file - {filename} is different between the local file system and the S3 bucket.')
            virtual_files.remove(file_name)
   virtual_disk[0].close()

## through boto3 resource
def get_files_on_s3_resource(bucket_name, folder_path):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    folder_objects = list(bucket.objects.filter(Prefix=folder_path))
    files_on_s3 = []
    for file in folder_objects:
        files_on_s3.append(file.key)
    return files_on_s3

## with paginator for list_objects_v2
def list_s3_objects_wp(bucket_name, folder_path):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')

    object_list = []
    for page in paginator.paginate(Bucket=bucket_name, Prefix=folder_path):
        for content in page.get('Contents', []):
            object_list.append(content)

    return object_list

## without paginator for list_objects_v2
def list_s3_objects_wop(bucket_name, folder_path):
    s3 = boto3.client('s3')
    # get list of files on s3
    object_list = []
    for obj in s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_path)['Contents']:
        object_list.append(obj)
        
    return object_list

## tried a way suggested in one of the answers above 
def list_s3_objects_so(bucket_name, folder_path):
    s3 = boto3.resource('s3')
    # get list of files on s3
    bucket = s3.Bucket(bucket_name)
    count_obj = sum(1 for _ in bucket.objects.filter(Prefix=folder_path))
    return count_obj

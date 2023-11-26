import boto3

def count_objects_in_s3_folder(bucket_name, folder_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Specify the bucket and prefix (folder) within the bucket
    bucket = {'Bucket': bucket_name}
    prefix = folder_name + '/'

    # Initialize the object count
    object_count = 0

    # Use the list_objects_v2 API to retrieve the objects in the folder
    paginator = s3.get_paginator('list_objects_v2')
    response_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

    # Iterate through the paginated responses
    for response in response_iterator:
        if 'Contents' in response:
            object_count += len(response['Contents'])

    print(f"Number of objects in folder '{folder_name}': {object_count}")

# Provide the S3 bucket name and folder name to count objects in
bucket_name = 'your_bucket_name'
folder_name = 'your_folder_name'

count_objects_in_s3_folder(bucket_name, folder_name)

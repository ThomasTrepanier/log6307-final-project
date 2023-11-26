s3 = boto3.resource('s3')

def upload_file_to_s3(s3_path, local_path):
    bucket = s3_path.split('/')[2] #bucket is always second as paths are S3://bucket/.././
    file_path = '/'.join(s3_path.split('/')[3:])
    response = s3.Object(bucket, file_path).upload_file(local_path)
    return response

s3_path = "s3://mybucket/sf_events.json"
local_path = "/home/ubuntu/bandsintown/sf_events.json"
upload_file_to_s3(s3_path, local_path)

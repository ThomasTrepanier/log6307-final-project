s3 = boto3.resource('s3')

def download_file_from_s3(s3_path, local_path):
    bucket = s3_path.split('/')[2] #bucket is always second as paths are S3://bucket/.././
    file_path = '/'.join(s3_path.split('/')[3:])
    filename = os.path.basename(s3_path) 
    s3.Object(bucket, file_path).download_file(local_file_path)

s3_path = "s3://mybucket/sf_events.json"
local_path = "/home/ubuntu/bandsintown/sf_events.json"
download_file_from_s3(s3_path, local_path)


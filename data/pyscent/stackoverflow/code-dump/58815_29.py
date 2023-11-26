def getNumberOfObjectsInBucket(bucketName,prefix):
    count = 0
    response = boto3.client('s3').list_objects_v2(Bucket=bucketName,Prefix=prefix)
    for object in response['Contents']:
        if object['Size'] != 0:
            #print(object['Key'])
            count+=1
    return count

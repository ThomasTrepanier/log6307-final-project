import boto3

# Set the endpoint URL globally
endpoint_url = 'https://your-custom-endpoint.amazonaws.com'
boto3.setup_default_session(region_name='us-east-1', endpoint_url=endpoint_url)

# Now all subsequent client/resource creation will use the configured endpoint URL
s3_client = boto3.client('s3')
sqs_resource = boto3.resource('sqs')

# Use the S3 client and SQS resource with the custom endpoint URL
s3_client.list_buckets()
sqs_resource.create_queue(QueueName='my-queue')

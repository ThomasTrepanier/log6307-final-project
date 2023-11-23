import boto3
from botocore.client import Config

# Configure the endpoint URLs for different services
s3_endpoint_url = 'http://localhost:4572'
sqs_endpoint_url = 'http://localhost:4576'

# Create custom session objects with different endpoint URLs
s3_session = boto3.session.Session()
sqs_session = boto3.session.Session()

s3_session.resource('s3').meta.client.meta.events.register(
    'choose-signer.s3.*', boto3.session.Session().get_default_s3_signer)
s3_session.client('s3').meta.events.register(
    'choose-signer.s3.*', boto3.session.Session().get_default_s3_signer)
s3_session.client('s3').meta.events.register(
    'choose-signer.s3.*', boto3.session.Session().get_default_s3_signer)

sqs_session.resource('sqs').meta.client.meta.events.register(
    'choose-signer.sqs.*', boto3.session.Session().get_default_s3_signer)
sqs_session.client('sqs').meta.events.register(
    'choose-signer.sqs.*', boto3.session.Session().get_default_s3_signer)
sqs_session.client('sqs').meta.events.register(
    'choose-signer.sqs.*', boto3.session.Session().get_default_s3_signer)

s3_session.client('s3').meta.events.register(
    'before-sign.s3', boto3.session.Session().inject_endpoint_url)
sqs_session.client('sqs').meta.events.register(
    'before-sign.s3', boto3.session.Session().inject_endpoint_url)

# Set the custom sessions as default session factories
boto3.setup_default_session(
    region_name='us-east-1', 
    botocore_session=s3_session,
    session=boto3.DEFAULT_SESSION)

boto3.setup_default_session(
    region_name='us-east-1', 
    botocore_session=sqs_session,
    session=boto3.DEFAULT_SESSION)

# Now all subsequent client/resource creation will use the registered sessions
s3_client = boto3.client('s3')
sqs_resource = boto3.resource('sqs')

# Use the S3 client and SQS resource with the custom endpoint URLs
s3_client.list_buckets()
sqs_resource.list_queues()

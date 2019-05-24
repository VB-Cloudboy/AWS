import boto3
import logging
from botocore.exceptions import ClientError

# Check for Exisiting buckets in my subscription
mybucket = boto3.client('s3', aws_access_key_id = 'MyAccessKey',
aws_secret_access_key = 'MySecretAccessKey')

lookup = mybucket.list_buckets()
print(lookup)

# Create new bucket 

def mynew_bucket(MyBucketName):
    ''' This function will initiate the bucket creation '''
s3 = boto3.client('s3')
try:
    s3.create_bucket(Bucket='MyBucketName')

except ClientError as e:
    logging.error(e)







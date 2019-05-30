import boto3
import os 

s3 = boto3.resource('s3', aws_access_key_id = 'MyAccessKey', aws_secret_access_key = 'MySecretAccessKey')

dataPath=(r'C:\Newfolder\*.zip');
myBucket='MyNewbucket';
fileName=os.listdir('c:\NewFolder')

for file in fileName:
	s3.meta.client.upload_file(dataPath, myBucket, file)
else:
	print("No file available for movement")


import boto3

s3 = boto3.resource('s3', aws_access_key_id = 'MyAccessKey', aws_secret_access_key = 'MySecretAccessKey')

dataPath=(r'C:\Newfolder\*.zip');
myBucket='MyNewbucket';
fileName=['localdata.zip','Myself.zip']

for file in fileName:
	s3.meta.client.upload_file(dataPath, myBucket, file)
else:
	print("No file available for movement")


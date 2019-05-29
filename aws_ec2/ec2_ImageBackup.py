import boto3
import datetime

''' Define EC2 and Authenticate AWS Account  '''
myec2 = boto3.client('ec2', aws_access_key_id = 'MyAccessKey', aws_secret_access_key = 'MySecretAccessKey', region_name='ap-south-1')

''' Initializing Variiables '''

date = datetime.datetime.utcnow().strftime('%d%m%Y')
ec2Id = 'i-xxxxxxxxxxxx'
name = "EC2_"+ ec2Id+"_ImageBackup_"+date

''' Defining Action '''
BackupAction = myec2.create_image(
	Name=ec2Id,
	Description='New_EC2-Instance_BackedUp_On_'+date,
	InstanceId=ec2Id,
	NoReboot=False
	)
print(name)
print(BackupAction)
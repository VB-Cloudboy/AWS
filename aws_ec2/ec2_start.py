import boto3

client = boto3.client('ec2', aws_access_key_id = 'MyAccessKey',
aws_secret_access_key = 'MySecretAccessKey', region_name = 'MyRegion' )

startInstance = client.start_instances(
    InstanceIds=['i-xxxxxxxxxxxx'] 
    )
print(startInstance)


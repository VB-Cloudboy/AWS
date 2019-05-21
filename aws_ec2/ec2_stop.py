import boto3

client = boto3.client('ec2', aws_access_key_id = 'MyAccessKey',
aws_secret_access_key = 'MySecretAccessKey', region_name = 'MyRegion' )

stopInstance = client.stop_instances(
    InstanceIds=['i-xxxxxxxxxxxx'],
    Force = True
    )
print(stopInstance)

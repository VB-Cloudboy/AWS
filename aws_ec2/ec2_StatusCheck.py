# Status Check of EC2 Instances

import boto3
import sys
from array import array

myec2 = boto3.client('ec2', aws_access_key_id = 'MyAccessKey',
aws_secret_access_key = 'MySecretAccessKey', region_name = 'MyRegion' )

mydevInstances = ['i-xxxxxxxxxxxxxxxxx']

for vm in mydevInstances:
    print(vm+' '+'is selected')
    rango = myec2.describe_instance_status(
        Filters=[            {
                'Name':'instance-state-name', 
                'Values':['running','stopped'] 
                },
                 ],
        InstanceIds=[ vm ])
    print(rango)
else:
    print("No EC2 Instances found in the region")

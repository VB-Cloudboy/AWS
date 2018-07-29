import datetime
import boto3

# Creating an SNS Client
client = boto3.client(
    "sns",
    aws_access_key_id= "MyAccessKeyID",
    aws_secret_access_key= "mySecretAccessKey",
    region_name="eu-west-1"
)

# Defining variables 
mydate= datetime.datetime.now()
day= mydate.strftime("%A")
date= mydate.strftime("%d")
month= mydate.strftime("%B")
year= mydate.strftime("%G")

print("Please pay an EMI of Rs 909/- for the month of" +' '+ month +' '+ "before" + ' ' + "7"+ month + year)

# Send Message to Individual
client.publish(
    PhoneNumber="+91XXXXXXXXX",
    Message="Please pay an EMI of Rs 909/- for the month of" +' '+ month +' '+ "before" + ' ' + "7"+ month + year +'.'+"\n"+ "\nRegards," + "\nCloudBoy" + "\n10010010000"
    )
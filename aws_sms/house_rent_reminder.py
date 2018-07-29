import datetime
import boto3

# Creating an SNS Client
client = boto3.client(
    "sns",
    aws_access_key_id= "MyAccessKeyID",
    aws_secret_access_key= "mySecretAccessKey",
    region_name="us-east-1"
)

# Defining variables 
mydate = datetime.datetime.now()
day= mydate.strftime("%A")
date= mydate.strftime("%d")
month= mydate.strftime("%B")
year= mydate.strftime("%G")

print("Please pay rent $500 for the month of" +' '+ month +' '+ "before" + ' ' + "17"+ month + year)

# Send Message to Individual
client.publish(
    PhoneNumber="+91XXXXXXXXX",
    Message="Please pay rent Rs 3000/- for the month of" +' '+ month +' '+ "before" + ' ' + "17"+ month + year +'.'+"\n"+ "\nRegards," + "\nCloudBoy" + "\n1001001000"
    )

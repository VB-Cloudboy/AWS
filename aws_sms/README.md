# SMS Notification using boto3 and AWS-SNS service
The intention of writing this python script was to notify;
	1. Remind my tenant to pay his monthly rent.
	2. Also, Notify one of my colleague to pay his debt which he took from me as a loan.

After successfully testing this scripts from my laptop, I deployed them in AWS lambda as a function
using cloudwatch events, configured them to notify the recipients on monthly basis.

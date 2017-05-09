# Automate EC2 AMI creation via Lambda 

This tool uses Lambda & Cloudwatch to automatically create EC2 AMIs at a scheduled time.

1. [Setup IAM Role](https://github.com/gaurav-kamboj/aws/tree/master/lambda-create-ami#setup-iam-role)
1. [Create Lambda Function](https://github.com/gaurav-kamboj/aws/tree/master/lambda-create-ami#create-lambda-function)
1. [Setup cron via Cloudwatch Events](https://github.com/gaurav-kamboj/aws/tree/master/lambda-create-ami#setup-cron-via-cloudwatch-events)


## Setup IAM Role

- Go to IAM 
- Click on Roles and then click "Create Role"
- In Select role type, select "AWS Lambda"

![](http://aws.gauravkamboj.com/images/iam-1.PNG)

- Provide EC2 access so that Lambda function can create AMIs

![](http://aws.gauravkamboj.com/images/iam-2.PNG)

* Provide a name and description for the role and click "Create Role".

![](http://aws.gauravkamboj.com/images/iam-3.PNG)

## Create Lambda function

![](http://aws.gauravkamboj.com/images/lambda-1.PNG)

![](http://aws.gauravkamboj.com/images/lambda-3.PNG)

![](http://aws.gauravkamboj.com/images/lambda-4.PNG)

![](http://aws.gauravkamboj.com/images/lambda-5.PNG)

Copy paste the Lambda function from [backup_instance_as_ami.py](https://github.com/rajgouravjain/devops/blob/master/aws/lambda/backup_instance_as_ami.py)

## Setup cron via Cloudwatch Events (to trigger Lambda function) 

- Go to Cloudwatch console. Click on Events - Rules. You will find the cron name which you created during the **Create Lambda function** step.
- Edit the rule and set the cron expression to the as per your desired time.

![](http://aws.gauravkamboj.com/images/cron-1.PNG)

To learn more on **how to setup cron expression for Cloudwatch Events** check - [https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions)


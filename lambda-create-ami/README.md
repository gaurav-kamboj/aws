# Automate AWS EC2 AMI creation via Lambda & CloudWatch

This tool uses AWS Lambda & CloudWatch to automatically create EC2 AMIs at a scheduled time.

**Usage**: 

- Setup AWS Lambda & CloudWatch as per below instructions. 
- Tag EC2 instances for which you want to automate AMI creation process with following tag: {Key: backup, Value: None}
- Update cron expression in AWS CloudWatch to meet your requirements.

**Credits for Lambda (python script) function** - [Rajgourav Jain](https://github.com/rajgouravjain)

1. [Setup IAM Role](https://github.com/gaurav-kamboj/aws/tree/master/lambda-create-ami#setup-iam-role)
1. [Create Lambda Function](https://github.com/gaurav-kamboj/aws/tree/master/lambda-create-ami#create-lambda-function)
1. [Setup cron via Cloudwatch Events](https://github.com/gaurav-kamboj/aws/tree/master/lambda-create-ami#setup-cron-via-cloudwatch-events-to-trigger-lambda-function)


## Setup IAM Role

- Go to IAM 
- Click on **Roles** and then click "**Create Rol**e"
- In Select role type, select "**AWS Lambda**"

![](http://aws.gauravkamboj.com/images/iam-1.PNG)

- **Provide EC2 access** so that Lambda function can create AMIs

![](http://aws.gauravkamboj.com/images/iam-2.PNG)

- Provide a name and description for the role and click "**Create Role**".

![](http://aws.gauravkamboj.com/images/iam-3.PNG)

## Create Lambda function

- Go to Lambda console and click on **Create a Lambda function**
- Click on **Blank Function**

![](http://aws.gauravkamboj.com/images/lambda-1.PNG)

- Click in the empty box and select **CloudWatch Events - Schedule** from the dropdown.

![](http://aws.gauravkamboj.com/images/lambda-3.PNG)

- **Configure Lambda Trigger** as per below screenshot and click **Next**

![](http://aws.gauravkamboj.com/images/lambda-4.PNG)

- **Configure Lambda Function** - add name and description. Select **Python 2.7** as runtime.
- Copy-paste the Lambda function from [backup_instance_as_ami.py](https://github.com/rajgouravjain/devops/blob/master/aws/lambda/backup_instance_as_ami.py)

![](http://aws.gauravkamboj.com/images/lambda-5.PNG)

- In the **Lambda function handler and role** section select **Choose an exisiting role**
- **Select IAM role created in step 1 for AWS Lambda function** in the dropdown. Keep rest of configuration as default and **create Lambda function**. 

![](http://aws.gauravkamboj.com/images/lambda-6.PNG)

## Setup cron via Cloudwatch Events (to trigger Lambda function) 

- Go to Cloudwatch console. Click on Events - Rules. You will find the cron name which you created during the **Create Lambda function** step.
- Edit the rule and set the cron expression as per your desired time.

![](http://aws.gauravkamboj.com/images/cron-1.PNG)

To learn more on **how to setup cron expression for Cloudwatch Events** check - [https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions)


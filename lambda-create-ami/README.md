# Automate EC2 AMI creation via Lambda 

This tool uses Lambda & Cloudwatch to automatically create EC2 AMIs at a scheduled time.

### **Setup IAM Role**

* Go to IAM 
* Click on Roles and then click "Create Role"
* In Select role type, select "AWS Lambda"

![](http://aws.gauravkamboj.com/images/iam-1.PNG)

* Provide EC2 access so that Lambda function can create AMIs

![](http://aws.gauravkamboj.com/images/iam-2.PNG)

* Provide a name and description for the role and click "Create Role".

![](http://aws.gauravkamboj.com/images/iam-3.PNG)

### **Create Lambda function**


![](http://aws.gauravkamboj.com/images/lambda-1.PNG)

![](http://aws.gauravkamboj.com/images/lambda-3.PNG)

![](http://aws.gauravkamboj.com/images/lambda-4.PNG)

![](http://aws.gauravkamboj.com/images/lambda-5.PNG)

Copy paste the Lambda function from [https://github.com/rajgouravjain/devops/blob/master/aws/lambda/backup_instance_as_ami.py](https://github.com/rajgouravjain/devops/blob/master/aws/lambda/backup_instance_as_ami.py)

Credits for Lambda function: [Rajgourav Jain](https://github.com/rajgouravjain) 

### Setup cron via Cloudwatch Events

- Go to Cloudwatch console. Click on Events - Rules. You will find the cron name which you created during the **Create Lambda function** step.

![](http://aws.gauravkamboj.com/images/cron-1.PNG)

To learn more on how to setup cron expression for Cloudwatch Event Rules check - [https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions)


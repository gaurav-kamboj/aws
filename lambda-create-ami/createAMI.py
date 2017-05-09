import os
import json
import datetime
import boto3
import boto3.session
from dateutil import parser

def lambda_handler(event, context):

    boto3_session = boto3.session.Session()

    #ec2_client = boto3_session.client('ec2')

    ec2_resource = boto3_session.resource('ec2')
    ec2_client = ec2_resource.meta.client

    ##print ec2_client.describe_instances()
    filter1 = [
     {
        'Name': 'tag:backup',
        'Values': ["*"]
     },
     {
        'Name' : 'instance-state-name',
        'Values': ['running']
     }
    ]
    #running_instances = None
    running_instances = []


    f1= ec2_client.describe_instances(DryRun=False,Filters=filter1)
    print "First Filter results is", json.dumps(f1, indent=4, sort_keys=True, default=str)
    #print "First Filter results is", json.dumps(f1["Reservations"][0]['Instances'], indent=4, sort_keys=True, default=str)
    if f1['Reservations']:

        for i  in f1["Reservations"][0]['Instances'] :
            running_instances.append(i['InstanceId'])
            instance = ec2_resource.Instance(i['InstanceId'])
            image = instance.create_image(  DryRun=False,
                Name=i['InstanceId'] + '-' + datetime.datetime.today().strftime('%Y-%m-%d-%H'),
                Description='Backup of Instance '+ i['InstanceId'] + " On " + datetime.datetime.today().strftime('%Y-%m-%d-%H') ,
                NoReboot=True
            )

    return running_instances

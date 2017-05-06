# Automated AMI Backups via Lambda
#
# Author: Gaurav Kamboj
# Version: 1.0.2

import boto3
import collections
import datetime
import sys
import pprint

ec = boto3.client('ec2')

def lambda_handler(event, context):
    
    reservations = ec.describe_instances(
        Filters=[
            {'Name': 'tag-key', 'Values': ['backup', 'Backup']},
        ]
    ).get(
        'Reservations', []
    )

    instances = sum(
        [
            [i for i in r['Instances']]
            for r in reservations
        ], [])

    print "Found %d instances that need backing up" % len(instances)

    to_tag = collections.defaultdict(list)

    for instance in instances:
        try:
            retention_days = [
                int(t.get('Value')) for t in instance['Tags']
                if t['Key'] == 'Retention'][0]
        except IndexError:
            retention_days = 7

            create_time = datetime.datetime.now()
            create_fmt = create_time.strftime('%Y-%m-%d')
        
            AMIid = ec.create_image(InstanceId=instance['InstanceId'], Name="Lambda - " + instance['InstanceId'] + " from " + create_fmt, Description="Lambda created AMI of instance " + instance['InstanceId'] + " from " + create_fmt, NoReboot=True, DryRun=False)

            
            pprint.pprint(instance)
            
            to_tag[retention_days].append(AMIid['ImageId'])
            
            print "Retaining AMI %s of instance %s for %d days" % (
                AMIid['ImageId'],
                instance['InstanceId'],
                retention_days,
            )

    print to_tag.keys()
    
    for retention_days in to_tag.keys():
        delete_date = datetime.date.today() + datetime.timedelta(days=retention_days)
        delete_fmt = delete_date.strftime('%m-%d-%Y')
        print "Will delete %d AMIs on %s" % (len(to_tag[retention_days]), delete_fmt)
    
        ec.create_tags(
            Resources=to_tag[retention_days],
            Tags=[
                {'Key': 'DeleteOn', 'Value': delete_fmt},
            ]
        )
    

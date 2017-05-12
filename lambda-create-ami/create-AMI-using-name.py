import datetime
import boto3
ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    reservations = ec2.describe_instances(
            Filters=[
                {'Name': 'tag-key', 'Values': ['backup', 'Backup']},
            ]
        ).get(
            'Reservations', []
    )

    def create_image(instance_id, instance_name, description, no_reboot=True, dry_run=False):
        AMIid = ec2.create_image(InstanceId=instance_id, Name=instance_name, Description=description, NoReboot=no_reboot, DryRun=dry_run)


    def get_instance_name(tags):
        for tag in tags:
            if tag['Key'] == 'Name':
                return '_'.join(tag['Value'].split())

    for reservation in reservations:
        create_time = datetime.datetime.now()
        create_fmt = create_time.strftime('%Y-%m-%d-%H')
        instance_name = get_instance_name(reservation.get('Instances')[0].get('Tags'))
        instance_name = instance_name + '_' + create_fmt
        instance_id = reservation.get('Instances')[0].get('InstanceId')
        description = instance_name
        create_image(instance_id, instance_name, description)

import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Connect to EC2
    ec2 = boto3.client('ec2')
    
    # Get all instances with the tag "sleeper" set to "true"
    instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:sleeper',
                'Values': ['true']
            }
        ]
    )['Reservations']
    
    # Get the instance IDs of all instances that are currently stopped
    stopped_instances = [instance['InstanceId'] for instance in instances if instance['State']['Name'] == 'stopped']
    
    # Start 10% of the stopped instances
    instances_to_start = stopped_instances[:int(len(stopped_instances) * 0.1)]
    ec2.start_instances(InstanceIds=instances_to_start)
    
    # Print the names of the instances that were started
    started_instances = ec2.describe_instances(InstanceIds=instances_to_start)['Reservations']
    for instance in started_instances:
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                print(tag['Value'])
import boto3
import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    instance_ids = []
    if current_time == "23:30":
        # filter instances by tag sleeper=true
        instances = ec2.describe_instances(Filters=[{'Name': 'tag:sleeper', 'Values': ['true']}])
        instances = instances['Reservations']
        instance_ids = [i['Instances'][0]['InstanceId'] for i in instances]
        ec2.stop_instances(InstanceIds=instance_ids)
    elif current_time == "05:30":
        if datetime.datetime.now().weekday() < 5:
            # filter instances by tag sleeper=true
            instances = ec2.describe_instances(Filters=[{'Name': 'tag:sleeper', 'Values': ['true']}])
            instances = instances['Reservations']
            instance_ids = [i['Instances'][0]['InstanceId'] for i in instances]
            ec2.start_instances(InstanceIds=instance_ids)
        else:
            instances = ec2.describe_instances(Filters=[{'Name': 'tag:sleeper', 'Values': ['true']}])
            instances = instances['Reservations']
            instance_ids = [i['Instances'][0]['InstanceId'] for i in instances]
            ec2.start_instances(InstanceIds=instance_ids[:int(len(instance_ids) * 0.1)])
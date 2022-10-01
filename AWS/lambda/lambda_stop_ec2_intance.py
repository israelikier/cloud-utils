# Dependency: ec2 instance tag - managed_poweroff = true
import boto3
ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    filters = [{'Name': 'tag:managed_poweroff', 'Values': ['true']}]
    ec2.instances.filter(Filters=filters).stop()
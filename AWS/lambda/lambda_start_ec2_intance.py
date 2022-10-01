# Dependency: ec2 instance tag - managed_poweron = true
import boto3
ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    filters = [{'Name': 'tag:managed_poweron', 'Values': ['true']}]
    ec2.instances.filter(Filters=filters).start()
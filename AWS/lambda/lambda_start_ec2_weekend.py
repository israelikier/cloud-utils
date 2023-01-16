import boto3

def lambda_handler(event, context):
  # Connect to EC2
  ec2 = boto3.client('ec2')

  # Get all instances with the tag "managed_poweron" set to "true"
  response = ec2.describe_instances(Filters=[{'Name': 'tag:managed_poweron', 'Values': ['true']}])
  instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

  # Start 10% of the instances
  to_start = int(len(instances) * 0.1)
  response = ec2.start_instances(InstanceIds=instances[:to_start])

  # Print the instances that were started
  print(f"Started instances: {response['StartingInstances']}")

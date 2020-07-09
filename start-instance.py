import boto3
region = 'us-east-1'
instance = ['COLOQUE O ID DA SUA INSTANCIA']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instance)
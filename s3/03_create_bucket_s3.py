import boto3

#Instantiate client conn
client = boto3.client('s3')

#set the new bucket name
bucket = 'handsonpythonnew'

#Create new bucket
client.create_bucket(Bucket=bucket)

#Retrieve all bucket Metada
response = client.list_buckets()

#loop trough bucjet data and display bucket names
for b in response['Buckets']:
    print(b['Name'])
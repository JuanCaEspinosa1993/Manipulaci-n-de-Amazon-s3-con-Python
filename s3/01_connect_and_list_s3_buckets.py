import boto3

#Instantiate a client
client = boto3.client("s3")

#Retrieve all bucket Metadata
response= client.list_buckets()

# loop troufh bucket data and displau bucket names
for b in response['Buckets']:
    print(b['Name'])
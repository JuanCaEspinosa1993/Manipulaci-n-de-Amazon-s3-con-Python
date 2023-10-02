import boto3

# client Instance
client = boto3.client('s3')

#Vars
bucket = 'handsonemptybucket'

#retrieve the bucket list
response = client.list_buckets()

for n in response['Buckets']:
    print(n['Name'])

client.delete_bucket(Bucket = bucket)
print('\nRemaining Buckets: ')

#retrieve the bucket list
response = client.list_buckets()

for n in response['Buckets']:
    print(n['Name'])
import boto3

# Client instance
client = boto3.client('s3')

# Variables
target_bucket = 'handsonpythonnew'
subfolder_01 = 'example/'
subfolder_02 = 'test_folder/'

# Create sufolder (Objects)
client.put_object(Bucket=target_bucket, Key=subfolder_01)
client.put_object(Bucket=target_bucket, Key=subfolder_02)

# Retrieve object info from bucket
all_objects = client.list_objects(Bucket=target_bucket)

# Iterate through Metada and list objects
for a in all_objects['Contents']:
    print(a['Key'], a['LastModified'])
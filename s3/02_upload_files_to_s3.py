import os
import boto3

# Instantiate client
client = boto3.client('s3')

#set variables
bucket = 'handsonpython'
cur_path = os.getcwd()
file = "Nominas_jc.xlsx"
filename = os.path.join(cur_path, 'data', file)

#Open the file
data = open(filename, "rb")

#load the data into s3
client.upload_file(filename, bucket, file)

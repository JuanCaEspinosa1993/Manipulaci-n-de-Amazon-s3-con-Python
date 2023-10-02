import os
import boto3

# client instance
client = boto3.client('s3')

#path and other variables
bucket = 'handsonpython'
cur_path = os.getcwd()
file = 'Nominas_jc.xlsx'
filename = os.path.join(cur_path, 'downloads', file)

# object method to download file
client.download_file(
    Bucket=bucket,
    Key=file,
    Filename=filename
)

# list the contents of DL dir
downloads_dir = os.path.join(cur_path, 'downloads')

for root, dirs, files in os.walk(downloads_dir):
    for fn in files:
        print(fn)
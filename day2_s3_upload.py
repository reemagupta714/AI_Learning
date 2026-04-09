print("Script started")
import boto3

# Create S3 client
s3 = boto3.client('s3')

# File details
file_name = 'day2_career_agent.py'
bucket_name = 'agentic-ai-reema-001'

# Upload file
s3.upload_file(file_name, bucket_name, file_name)

print("File uploaded successfully to S3")
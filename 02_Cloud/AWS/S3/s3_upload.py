import boto3

print("=== S3 Upload Tool ===")

# Take input from user
file_name = input("Enter file name to upload: ")
bucket_name = input("Enter bucket name: ")

try:
    s3 = boto3.client('s3')

    s3.upload_file(file_name, bucket_name, file_name)

    print("File uploaded successfully to S3")

except Exception as e:
    print("Error occurred:", e)
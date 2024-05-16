import b2sdk.v1 as b2

# Initialize B2 API client with application key ID and application key
info = b2.InMemoryAccountInfo()
b2_api = b2.B2Api(info)
application_key_id = 'YOUR_APPLICATION_KEY_ID'
application_key = 'YOUR_APPLICATION_KEY'
b2_api.authorize_account("production", application_key_id, application_key)

# Get the bucket that you want to upload files to
bucket_name = 'YOUR_BUCKET_NAME'
bucket = b2_api.get_bucket_by_name(bucket_name)

# Upload a file to the bucket
file_path = 'path/to/your/file.jpg'
with open(file_path, 'rb') as file:
    bucket.upload_bytes(file.read(), 'file.jpg')

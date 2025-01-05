


def create_bucket(storage_client, bucket_name):
    bucket = storage_client.create_bucket(bucket_name)

    print(" >> Bucket created")


def upload_file(storage_client, bucket_name, src_file, dst_file):

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(dst_file)
    blob.upload_from_filename(src_file)

    print('>> Uploaded')


def download_file(storage_client, bucket_name, src_file, dst_file):

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(dst_file)
    blob.download_to_filename(src_file)

    print('>> Downloaded')
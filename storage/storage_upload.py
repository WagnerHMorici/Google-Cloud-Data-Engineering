from google.cloud import storage

import config 
from utils import upload_file

service_account_json_path = config.GCP_SERVICE_ACCOUNT_PATH
bucket_name = config.GCS_BUCKET


storage_client = storage.Client.from_service_account_json(service_account_json_path)


upload_file(storage_client, bucket_name, 'storage\Toyota_Data.csv', 'test_storage\Toyota_Data.csv')
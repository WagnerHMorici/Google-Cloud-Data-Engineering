from google.cloud import storage

from utils import create_bucket
import config


service_account_json_path = config.GCP_SERVICE_ACCOUNT_PATH
bucket_name = config.GCS_BUCKET


print(service_account_json_path)
storage_client = storage.Client.from_service_account_json(service_account_json_path)




create_bucket(storage_client, bucket_name)

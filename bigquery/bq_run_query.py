from google.cloud import bigquery
from google.api_core.exceptions import Conflict

from utils import query_data
import config


service_account_json_path = config.GCP_SERVICE_ACCOUNT_PATH
dataset_name = config.BQ_DATASET
table_name = config.BQ_TABLE


bigquery_client = bigquery.Client.from_service_account_json(service_account_json_path)

query = f'''SELECT Date, Close from {dataset_name}.{table_name}'''

data = query_data(bigquery_client, dataset_name, table_name, query)

for row in data:
    print(row)
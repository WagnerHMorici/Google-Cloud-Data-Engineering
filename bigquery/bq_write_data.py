from google.cloud import bigquery
from google.api_core.exceptions import Conflict

from utils import write_data, read_csv
import config


service_account_json_path = config.GCP_SERVICE_ACCOUNT_PATH
dataset_name = config.BQ_DATASET
table_name = config.BQ_TABLE
path = config.CSV_PATH


bigquery_client = bigquery.Client.from_service_account_json(service_account_json_path)

data = read_csv(path)

write_data(bigquery_client, dataset_name, table_name,data)




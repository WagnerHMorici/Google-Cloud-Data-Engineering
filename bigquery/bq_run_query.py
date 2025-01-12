from google.cloud import bigquery
from google.api_core.exceptions import Conflict

from utils import create_dataset, create_table
import config


service_account_json_path = config.GCP_SERVICE_ACCOUNT_PATH
dataset_name = config.BQ_DATASET
table_name = config.BQ_TABLE


bigquery_client = bigquery.Client.from_service_account_json(service_account_json_path)

write_data(bigquery_client, dataset_name)


schema = [
    bigquery.SchemaField("Date", "DATE", mode="REQUIRED"),
    bigquery.SchemaField("Adj Close", "FLOAT", mode="REQUIRED"),
    bigquery.SchemaField("Close", "FLOAT", mode="REQUIRED"),
    bigquery.SchemaField("High", "FLOAT", mode="REQUIRED"),
    bigquery.SchemaField("Low", "FLOAT", mode="REQUIRED"),
    bigquery.SchemaField("Open", "FLOAT", mode="REQUIRED"),
    bigquery.SchemaField("Volume", "FLOAT", mode="REQUIRED"),
]

create_table(bigquery_client, dataset_name, table_name, schema)
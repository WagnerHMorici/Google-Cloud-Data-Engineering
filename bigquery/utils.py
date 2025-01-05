from google.cloud import bigquery


def create_dataset(bigquery_client, dataset_name):
    dataset_id = f"{bigquery_client.project}.{dataset_name}"
    dataset_ref = bigquery.Dataset(dataset_id)


    dataset = bigquery_client.create_dataset(dataset_ref, exists_ok=True)

    print(">> Dataset Created ")

def create_table(bigquery_client, dataset_name, table_name, schema):
    
    dataset_ref = bigquery_client.dataset(dataset_name)

    table_ref = dataset_ref.table(table_name)

    table = bigquery.Table(table_ref, schema)
    table = bigquery_client.create_table(table)

    print('>> Table created')

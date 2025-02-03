from google.cloud import bigquery

import csv


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


def write_data(bigquery_client, dataset_name, table_name, data):
    
    dataset_ref = bigquery_client.dataset(dataset_name)

    table_ref = dataset_ref.table(table_name)

    table = bigquery_client.get_table(table_ref)
    
    bigquery_client.insert_rows(table, data)

    print('>> Inserted Data')
    

def read_csv(path):
    with open(path, 'r') as fl:
        reader = csv.reader(fl, delimiter=',')
        data = list(reader)[1:]

    return data


def query_data(bigquery_client, dataset_name, table_name, query):
    
    query = bigquery_client.query(query)

    
    results = query.result()
    
    return results
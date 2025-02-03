
# Toyota Stocks Data Pipeline

This project aims to extract data on Toyota's stock, manipulate it on Google Cloud Platform (GCP) using services like Google Cloud Storage (GCS) and BigQuery.

## Description

The data pipeline extracts historical stock data for Toyota, stores it on Google Cloud Storage, and processes it with BigQuery for subsequent analysis. The pipeline involves the following steps:

1. **Data Extraction:** Collects Toyota's stock data in CSV format.
2. **Storage:** The CSV data is uploaded to a GCS bucket.
3. **Processing:** The data is loaded into BigQuery for manipulation and analysis.

## Requirements

Before running the project, ensure you have the following set up:

- A Google Cloud Platform (GCP) account: [GCP Account](https://cloud.google.com/)
- A GCP project with access to **Storage** and **BigQuery** services
- A GCP service account with appropriate permissions (see [how to create and configure](https://cloud.google.com/docs/authentication/getting-started))
- Python 3.x
- Required Python libraries: `google-cloud-storage`, `google-cloud-bigquery`, `requests` (for data fetching)

## Configuration

### Environment Variables

GCP_SERVICE_ACCOUNT_PATH=/path/to/your/service/account/key.json
GCP_PROJECT_ID=your-gcp-project-id
GCP_REGION=your-gcp-region
GCP_ZONE=your-gcp-zone
GCS_BUCKET=your-gcs-bucket-name
CSV_PATH=path/to/your/csv/file.csv
BQ_DATASET=your-bigquery-dataset
BQ_TABLE=your-bigquery-table-name

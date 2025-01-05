from decouple import config as dconfig

GCP_SERVICE_ACCOUNT_PATH = dconfig('GCP_SERVICE_ACCOUNT_PATH')
GCP_PROJECT_ID = dconfig('GCP_PROJECT_ID')
GCP_REGION = dconfig('GCP_REGION')
GCP_ZONE = dconfig('GCP_ZONE')


GCS_BUCKET = dconfig('GCS_BUCKET')
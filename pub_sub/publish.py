from google.cloud import pubsub_v1
from google.api_core.exceptions import Conflict

from utils import create_topic,data_publisher
import config


service_account_json_path = config.GCP_SERVICE_ACCOUNT_PATH
topic_name = config.TOPIC_NAME

data = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          -46.54461301004548,
          -23.7157563074841
        ],
        "type": "Point"
      }
    }
  ]
}


publisher_client = pubsub_v1.PublisherClient.from_service_account_json(service_account_json_path)

create_topic(publisher_client, topic_name)

data_publisher(publisher_client, topic_name, data)

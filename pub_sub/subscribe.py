from google.cloud import pubsub_v1
from google.api_core.exceptions import Conflict

from utils import create_topic,data_publisher
import config


service_account_json_path = config.GCP_SERVICE_ACCOUNT_PATH
topic_name = config.TOPIC_NAME



subscriber_client = pubsub_v1.SubscriberClient.from_service_account_json(service_account_json_path)

create_topic(publisher_client, topic_name)

data_publisher(publisher_client, topic_name, data)

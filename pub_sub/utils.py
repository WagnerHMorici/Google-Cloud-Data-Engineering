
import json

def create_topic(pub_client, topic_name):
    
    topic = pub_client.create_topic(name=topic_name)

    print("Topic created")



def data_publisher(pub_client, topic_name,data):
    bytes_data = json.dumps(data).encode("utf-8")

    res = pub_client.publish(topic_name, bytes_data)

    print(res.result())


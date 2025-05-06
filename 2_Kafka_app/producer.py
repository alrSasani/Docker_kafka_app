from confluent_kafka import Producer
import socket
import requests
import time
import json


KAFKA_BROKER = "kafka:9092"  # Use your Kafka container's service name
TOPIC = "test-topic"

producer = Producer({'bootstrap.servers': KAFKA_BROKER})

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def produce(topic, message):
    producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
    producer.flush()

if __name__ == '__main__':

    while True:
        usr_dict = requests.get("http://user_api:5000/user").json()
        # if res.lower() == 'exit':
        #     break
        print(usr_dict)
        produce('test-topic', json.dumps(usr_dict))
        time.sleep(4)
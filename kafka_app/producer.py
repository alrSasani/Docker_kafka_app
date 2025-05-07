from confluent_kafka import Producer
import socket
import requests
import time
import json
import os


TOPIC=os.environ.get('TOPIC')
KAFKA_BROKER=os.environ.get('KAFKA_BROKER')

producer = Producer({'bootstrap.servers': KAFKA_BROKER})

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


def produce(topic, message):
    producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
    producer.flush()

def produce_user_data(waint_time=4):
    while True:
        usr_dict = requests.get("http://user_api:5000/user").json()
        # if res.lower() == 'exit':
        #     break
        print(usr_dict)
        produce(TOPIC, json.dumps(usr_dict))
        time.sleep(waint_time)

if __name__ == '__main__':
    produce_user_data(waint_time=4)

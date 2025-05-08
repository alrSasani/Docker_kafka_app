# tests/test_kafka.py
from kafka import KafkaProducer, KafkaConsumer
import json

def test_kafka_production():
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    test_data = {"test": "data"}
    producer.send('test_topic', value=test_data)
    producer.flush()

def test_kafka_consumption():
    consumer = KafkaConsumer(
        'test_topic',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    # You'll need to produce a message first in setup
    for message in consumer:
        assert message.value["test"] == "data"
        break
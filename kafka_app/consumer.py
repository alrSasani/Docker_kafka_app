from confluent_kafka import Consumer, KafkaException
from db_connector import get_pg_conn, get_mongo_coll
from db_io import write_to_mongo, write_to_pg
import json
import os

# KAFKA_BROKER = "kafka:9092"  
# TOPIC = "user_topic"
TOPIC=os.environ.get('TOPIC')
KAFKA_BROKER=os.environ.get('KAFKA_BROKER')


consumer = Consumer({
        'bootstrap.servers': KAFKA_BROKER,
        'group.id': 'python-consumer',
        'auto.offset.reset': 'earliest'
    })
consumer.subscribe([TOPIC])

def consume():
    pg_conn = get_pg_conn()
    mongo_coll=get_mongo_coll()
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            data_dict = json.loads(msg.value().decode("utf-8")) 
            write_to_pg(pg_conn,data_dict)
            write_to_mongo(mongo_coll,data_dict)
            print(data_dict)

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    consume()
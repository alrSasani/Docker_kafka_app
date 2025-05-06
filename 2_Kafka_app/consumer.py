from confluent_kafka import Consumer, KafkaException

KAFKA_BROKER = "kafka:9092"  # Use your Kafka container's service name
TOPIC = "test-topic"

consumer = Consumer({
        'bootstrap.servers': KAFKA_BROKER,
        'group.id': 'python-consumer',
        'auto.offset.reset': 'earliest'
    })
consumer.subscribe(['test-topic'])

def consume():
    try:
        cons_file = open("consume_text.txt","w")
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
            print(f'Received message: {msg.value().decode("utf-8")}')
            cons_file.write(msg.value().decode("utf-8"))
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    consume()
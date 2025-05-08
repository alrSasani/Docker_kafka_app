# tests/integration/test_api_kafka.py
def test_user_creation_produces_kafka_message():
    # Create user via API
    response = client.post(...)
    
    # Consume from Kafka
    consumer = KafkaConsumer(...)
    for message in consumer:
        assert message.value["email"] == "test@example.com"
        break
# tests/e2e/test_full_pipeline.py
def test_full_pipeline():
    # 1. Create via API
    response = client.post(...)
    
    # 2. Check Kafka
    consumer = KafkaConsumer(...)
    kafka_message = None
    for msg in consumer:
        if msg.value["email"] == "e2e@test.com":
            kafka_message = msg.value
            break
    
    # 3. Check databases
    sql_user = sql_session.query(User).filter_by(email="e2e@test.com").first()
    mongo_user = mongo_db.users.find_one({"email": "e2e@test.com"})
    
    assert kafka_message
    assert sql_user
    assert mongo_user
    
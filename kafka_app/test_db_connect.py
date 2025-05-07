from pymongo import MongoClient
import psycopg2
import time

def get_mongo_coll(client="mongo",mongo_db="streamDB",collection="users"):
    mongo_client = MongoClient(client, 27017)
    mongo_db = mongo_client[mongo_db]
    mongo_collection = mongo_db[collection]
    return mongo_collection
    
def get_pg_conn(dbname="streamDB", user="kafka", password="kafkapass", host="postgres"):
    while True:
        try:
            pg_conn = psycopg2.connect(
                dbname=dbname, user=user, password=password, host=host
            )
            break
        except:
            print("Waiting for PostgreSQL...")
            time.sleep(2)

    pg_cursor = pg_conn.cursor()
    pg_cursor.execute("CREATE TABLE IF NOT EXISTS data (first_name TEXT, last_name TEXT, age int, phone_number bigint, city text, country text);")
    pg_conn.commit()
    return pg_conn


if __name__=="__main__":
    import os

    PG_USER = os.environ.get('POSTGRES_USER')
    PG_PASS = os.environ.get('POSTGRES_PASSWORD')
    PG_DB = os.environ.get('POSTGRES_DB')
    MONGO_CLIENT=os.environ.get('Mongo_client')
    MONGO_DB=os.environ.get('Mongo_db')
    MONGO_COLL=os.environ.get('Mongo_Collection')
    TOPIC=os.environ.get('TOPIC')
    KAFKA_BROKER=os.environ.get('KAFKA_BROKER')

    print(TOPIC,KAFKA_BROKER)
    conne = get_pg_conn()
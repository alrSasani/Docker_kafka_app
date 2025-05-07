from pymongo import MongoClient
import psycopg2
import time


def write_to_pg(pg_conn,user_data):
    pg_cursor = pg_conn.cursor()
    pg_cursor.execute(
    "INSERT INTO user_data (first_name, last_name, age, phone_number, city, country) VALUES (%s, %s, %s, %s, %s, %s)",
    (user_data.get("first_name"), user_data.get("last_name"), user_data.get("age"), user_data.get("phone"), user_data.get("city"), user_data.get("country"))
        )
    
    pg_conn.commit()

def write_to_mongo(mongo_collection,user_data):
    # Save to MongoDB
    mongo_collection.insert_one(user_data)
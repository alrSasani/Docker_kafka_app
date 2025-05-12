# tests/test_kafka.py
from confluent_kafka import Producer, Consumer
import requests
import time
import json
import os
from db_connector import get_pg_conn, get_mongo_coll
from db_io import write_to_mongo, write_to_pg

def test_consumer():
    pass

def test_producer():
    pass
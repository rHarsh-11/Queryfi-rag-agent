import os
import re
import logging
from pymongo import MongoClient
from bson import ObjectId
import json5
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "valuefy")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME", "clients")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in environment variables.")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

def serialize_mongo_result(docs):
    return [{**doc, "_id": str(doc["_id"])} for doc in docs]

def fetch_from_mongo(query: str):
    """
    Execute a MongoDB find query passed as a string (e.g., 'db.clients.find({"active": true})')
    """
    pattern = r"\.find\(\s*({(?:[^{}]|{[^{}]*})*})\s*(?:,\s*({(?:[^{}]|{[^{}]*})*}))?\s*\)"
    match = re.search(pattern, query, re.DOTALL)

    if not match:
        filter_query = {}
        projection = None
        logging.info("No .find() filter found. Using empty filter.")
    else:
        filter_str = match.group(1)
        projection_str = match.group(2)

        try:
            filter_query = json5.loads(filter_str)
        except Exception as e:
            logging.error(f"Failed to parse filter JSON: {filter_str} | Error: {e}")
            filter_query = {}

        if projection_str:
            try:
                projection = json5.loads(projection_str)
            except Exception as e:
                logging.error(f"Failed to parse projection JSON: {projection_str} | Error: {e}")
                projection = None
        else:
            projection = None

    logging.info(f"Running MongoDB find with filter: {filter_query} and projection: {projection}")

    try:
        if projection:
            cursor = collection.find(filter_query, projection)
        else:
            cursor = collection.find(filter_query)
        results = list(cursor)
        return serialize_mongo_result(results)
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        return []


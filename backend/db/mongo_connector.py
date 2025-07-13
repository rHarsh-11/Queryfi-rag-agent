from pymongo import MongoClient
from bson import ObjectId
import re
import logging
import json5

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://harsh:strongpassword@valuefy.t8m9ka9.mongodb.net/?retryWrites=true&w=majority&appName=valuefy")
db = client["valuefy"]
collection = db["clients"]

def serialize_mongo_result(docs):
    serialized = []
    for doc in docs:
        doc["_id"] = str(doc["_id"])
        serialized.append(doc)
    return serialized

def fetch_from_mongo(query: str):
    import logging
    logging.basicConfig(level=logging.INFO)

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

    if projection:
        cursor = collection.find(filter_query, projection)
    else:
        cursor = collection.find(filter_query)

    results = list(cursor)
    return serialize_mongo_result(results)

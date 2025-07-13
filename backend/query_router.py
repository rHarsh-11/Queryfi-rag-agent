from db.mongo_connector import fetch_from_mongo
from db.mysql_connector import fetch_from_mysql
from utils.format_response import format_result


def execute_query_from_prompt(query: str):
    query_lower = query.lower()
    if "find" in query_lower or "mongo" in query_lower or "collection" in query_lower:
        print("\nRouting to MongoDB")
        raw = fetch_from_mongo(query)
        print("Raw MongoDB Result:", raw)
    elif "select" in query_lower or "from" in query_lower:
        print("\nRouting to MySQL")
        raw = fetch_from_mysql(query)
    else:
        raise ValueError("Unknown or unsupported query type.")

    return format_result(raw)

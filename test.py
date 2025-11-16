from pymongo import MongoClient

uri = "mongodb+srv://rajemohit330_db_user:mohit123@cluster0.r3pjezo.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(uri)
    print("Connected Successfully!")
    print(client.list_database_names())
except Exception as e:
    print("Error:", e)

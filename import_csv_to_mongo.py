import csv
from pymongo import MongoClient

def import_csv_to_mongo(csv_file_path, db_name, collection_name, mongo_uri):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        records = [row for row in reader]
        
    if records:
        collection.insert_many(records)
        print(f"Imported {len(records)} records into {collection_name}")
    else:
        print("No records found in the CSV file.")

    client.close()


db_name = 'test'
collection_name = 'Assignment2'
mongo_uri = 'mongodb://localhost:27017'

import_csv_to_mongo(csv_file_path, db_name, collection_name, mongo_uri)

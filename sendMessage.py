from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# client = MongoClient(os.getenv('DB_SERVER'))

# db = client["mongodbVSCodePlaygroundDB"] os.getenv('DB_SERVER')

client = MongoClient("mongodb+srv://ernhoohacks23:tDN6WK1x2XnsGtby@erncluster0.wsxs09g.mongodb.net/?retryWrites=true&w=majority")
db = client.mongodbVSCodePlaygroundDB

responses_in_db = db["responses"]


def create_new_document(message):
    # Setting up document file
    
    new_doc = {
        'location':"1010 River St, Austin, Texas USA",
        'type':'Medical Emergency',
        'text_msg':f'{message}'
    }

    return new_doc


def insert_new_response(new_response):
    collection = db['responses']
    doc1 = create_new_document("Testing Document")
    collection.insert_one(doc1)
    print("Done")

insert_new_response("")
    




# # List all collections in the database
# collection_names = db.list_collection_names()

# # Print the collection names
# for name in collection_names:
#     print(name)



# db = client['mongodbVSCodePlaygroundDB']
# collection = db['responses']
# doc_count = collection.count_documents({})
# print(doc_count)



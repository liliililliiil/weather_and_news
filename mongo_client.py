from pymongo import MongoClient
import pandas as pd
import json


URI = "mongodb+srv://rusfhr:rkdrudfhr12!!@cluster0.e6omr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

with open("C:/Users/nsa28/OneDrive/바탕 화면/Visual Studio Code File/cs_project/section3_proj/서울경기1973_2022기온분석.json", encoding='utf-8') as f:
    data = json.load(f)

HOST = 'cluster0.e6omr.mongodb.net'
USER = 'rusfhr'
PASSWORD = 'rkdrudfhr12!!'
DATABASE_NAME = 'cs_project'
COLLECTION_NAME = 'sg_temp'

URI = "mongodb+srv://{}:{}@{}/{}?retryWrites=true&w=majority".format(USER, PASSWORD, HOST, DATABASE_NAME)
client = MongoClient(URI)

DATABASE = 'cs_project'
database = client[DATABASE]

collection = database[COLLECTION_NAME]

collection.insert_many(documents=data)
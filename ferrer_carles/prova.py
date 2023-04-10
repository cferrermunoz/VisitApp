import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongodb = os.getenv("mongodb")
user = os.getenv("user")
password = os.getenv("password")
client = MongoClient("mongodb+srv://" + user + ":" + password + mongodb)
db = client.cferrer1
agenda = db.METGES.find_one({},{'agenda': 1})
for x in agenda['agenda']:
    if x['moment_visita'].strftime('%Y-%m-%d') == "2023-04-13" and x['id_pacient'] == 0:
        print(x)


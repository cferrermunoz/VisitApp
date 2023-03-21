import os, pandas
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime
load_dotenv()
mongodb = os.getenv("mongodb")
user = os.getenv("user")
password = os.getenv("password")
client = MongoClient("mongodb+srv://"+user+":"+password+mongodb)

excelUsuaris = pandas.read_excel("Tasca3.xlsx", sheet_name="USUARIS")
excelVisites = pandas.read_excel("Tasca3.xlsx", sheet_name="VISITES")
excelHoraris = pandas.read_excel("Tasca3.xlsx", sheet_name="HORARIS")

list_usuaris = excelUsuaris.to_dict(orient="records")
list_visites = excelVisites.to_dict(orient="records")
list_horaris = excelHoraris.to_dict(orient="records")

db = client.cferrer1
for row in list_visites:
    id_metge = row.pop("id_temporal_metge")
    id_pacient = row.pop("id_temporal_pacient")
    print(id_metge, id_pacient)
    login_metge = ""
    login_pacient = ""
    for user in list_usuaris:
        if user["id_temporal"] == id_metge:
            login_metge = user["login"]
            print(login_metge)
    for user in list_usuaris:
        if user["id_temporal"] == id_pacient:
            login_pacient = user["login"]
            print(login_pacient)
client.close()
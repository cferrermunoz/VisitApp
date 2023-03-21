import datetime
import os, pandas
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import *

#load excel files

excelUsuaris = pandas.read_excel("Tasca3.xlsx", sheet_name="USUARIS")
excelVisites = pandas.read_excel("Tasca3.xlsx", sheet_name="VISITES")
excelHoraris = pandas.read_excel("Tasca3.xlsx", sheet_name="HORARIS")

list_usuaris = excelUsuaris.to_dict(orient="records")
list_visites = excelVisites.to_dict(orient="records")
list_horaris = excelHoraris.to_dict(orient="records")

load_dotenv()
mongodb = os.getenv("mongodb")
user = os.getenv("user")
password = os.getenv("password")
client = MongoClient("mongodb+srv://"+user+":"+password+mongodb)

db = client.cferrer1

usuaris_collection = db.USUARIS
metges_collection = db.METGES
pacients_collection = db.PACIENTS

usuaris_collection.drop()
metges_collection.drop()
pacients_collection.drop()

# for x in list_visites:
#     print(x)
# for x in list_horaris:
#     print(x)

for x in list_usuaris:
    numero_mutua = x.pop("Num_mutualista")
    mutua = x.pop("Mutua")
    idtemporal = x.pop("id_temporal")
    Especialitat = x.pop("Especialitat")
    num_col = x.pop("Num_colegiat")
    nomicog = x.pop("Cognoms,_i_Nom")
    nomicogs = nomicog.partition(',')
    cognoms = nomicogs[0].partition(' ')
    x["cognom1"] = cognoms[0]
    x["cognom2"] = cognoms[2]
    nom=nomicogs[2]
    x["nom"] = nom[1:]
    x["password"] = ""
    if(pandas.isna(x["DNI"])):
        x.pop("DNI")
        x["DNI"]=""
    sexe=x.pop("Sexe")
    if(sexe==1):
        x["Sexe"]="F"
    else:
        x["Sexe"] = "M"
    strdate = x.pop("Data_Naixement")
    x["data_naix"] = datetime.strptime(strdate, '%Y-%m-%dT%H:%M:%S.%fZ')
    afegir = usuaris_collection.insert_one(x).inserted_id
    if (pandas.notna(Especialitat)):
        y = {"_id":afegir}
        y["especialitat"]=Especialitat
        y["num_colegiat"]=num_col
        for t in list_horaris:
            if t["id_temporal_metge"]==idtemporal:
                # print(t)
                agenda=[]
                # data = datetime.strptime("2023-01-02T09:00:00.00Z", '%Y-%m-%dT%H:%M:%S.%fZ')
                # while data < datetime.strptime("2023-06-30T00:00:00.n", '%Y-%m-%dT%H:%M:%S.%fZ'):
                #     for v in list_horaris:
                #         if v["id_temporal_metge"]==idtemporal:
                #             if v["Dilluns"]=="s":
                #                 print()
                #                 agenda.append({"dia":data})
                #                 data = data +datetime.timedelta(minutes=30)
        y["agenda"]=agenda
        metges_collection.insert_one(y)
    if (pandas.notna(mutua)):
        z = {"_id":afegir}
        z["mutua"]=mutua
        z["num_mutua"]=numero_mutua
        pacients_collection.insert_one(z)

excelUsuaris = pandas.read_excel("Tasca3.xlsx", sheet_name="USUARIS")
list_usuaris = excelUsuaris.to_dict(orient="records")

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
            break
    for user in list_usuaris:
        if user["id_temporal"] == id_pacient:
            login_pacient = user["login"]
            print(login_pacient)
            break
    hora = row.pop("Moment_visita")
    print(hora)
    # db.metges_collection.update_one()

# print(db.list_collection_names())
client.close()
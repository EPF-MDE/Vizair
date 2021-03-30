from sources.database import mongoClient, heroDto
from bson.json_util import dumps
import json

def Get(id):
    with mongoClient.connect() as client:
        database = client[mongoClient.DatabaseName]
        result = database.heroes.find_one({'id': id })
        return result

def GetAll():
    with mongoClient.connect() as client:
        database = client[mongoClient.DatabaseName]
        result = database.heroes.find()
        return result
# coding=utf-8
from pymongo import MongoClient
from bson.code import Code

client = MongoClient()
db = client.journey


def UserSingnUp(userData):
#    if(db.userData.find({"username": userData["username"]}).count()==1):
#       return "-1"
#   else:
#       db.userData.save({"username": userData["username"],"password1": userData["password1"],"email": userData["email"]})
        return userData


def UserSingnIn(userData):
    data = db.userData.find({"username": userData["username"]})
    print data.count
    if(data.count()!=1):
        return "-1"
    user = data.next();
    print user["username"]
    if(user["password1"] != userData["username"]) :
        return -2
    else :
        return data
#12345678765432
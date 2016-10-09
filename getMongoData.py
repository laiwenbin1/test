# coding=utf-8
from pymongo import MongoClient
from bson.code import Code

client = MongoClient()
db = client.journey
cureData = db.data

map = Code("""
function (){
   var  s = this.治疗属性
   for(var  i = 0 ; i<s.length; i++){
   var result = s[i]["治疗次信息"][0]
       for(var key in result) {
          emit(key,1)
          }
      }
}
""")
reduce = Code("""
function (key,values){
  var sum = 0 ;
    for(var s = 0 ; s < values.length ; s++ ){
      sum += values[s]
      }
  return sum;
}
""")
db.data.map_reduce(map, reduce, "temp")
for x in db.temp.find():
    print x["value"];
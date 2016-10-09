# coding=utf-8
from pymongo import MongoClient
from bson.code import Code

client = MongoClient()
db = client.journey
cureData = db.data



sum = 0 ;
for x in db.temp.find():
    sum += x["value"]
print sum

# 获取医疗数据统计接受 手术，化疗，放疗  治疗的病人人数 ；
def getMedicalData():
     map = Code( """
function (){
    var one = 1 ;
    var  s = this.治疗属性
    var temp = "" ;
    var b = "" ;
    for(var  i = 0 ; i < s.length; i++){
       var result = s[i]["治疗次信息"]
       for(var  y = 0 ; y < result.length; y++)
           for(var key in result[y]) {
              if(key == "介入元素" || key == "实验室检查"  || key == "免疫治疗元素" || b == key ){break;}
              temp += " "+key
              emit(key,one)
              b = key ;
              }
          }
           if(temp.length > 5 ) {
               var s = "" ;
               var a = temp.split(" ").sort()
               for(var  i = 0 ; i < a.length; i++){
                   s+=a[i]
                   }
               emit(s,one)
           }
}
    """ )
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

     #db.temp.ecreateIndex({ "value": -1})
     result = db.temp.find()
     daresult = ""
     for x in result:
         daresult +=  x["_id"] +";"+ str(x["value"]) + ";"
     return daresult

#统计原发部位top10.

def occurrence():
    dict_pri = {}
    c = db.data.aggregate(
        [{'$group': {"_id": {"诊断名称": "$疾病属性.疾病确认.原发部位"},'total': {'$sum': 1}}}  , {'$sort': {"total": -1}} , {'$limit':10 }  ])
    for a in c:
          db.TopPart.save({'part':a[u'_id'][u'\u8bca\u65ad\u540d\u79f0'] ,'total': a[u'total']})
def get_occurrence_t():
     daresult = ""
     for x in db.TopPart.find():
         daresult += str(x["total"]) + ";" + str(x["part"]) + ";"
     return daresult


def get_occurrence():
    return db.TopPart.find()



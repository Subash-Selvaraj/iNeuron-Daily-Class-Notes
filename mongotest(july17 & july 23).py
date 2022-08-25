#basics of the mongo db connection to the cluster #mongo db comes under the NOSQL which means not only sql is act like a database
import pymongo


# #if our password of cluster is having @ and then we have to use this below method other wise we can just call the cluster simply
# import urllib.parse
# username = urllib.parse.quote_plus('subash032')
# password = urllib.parse.quote_plus("S@mcas2017")
# url =pymongo.MongoClient("mongodb+srv://{}:{}@subash.k8i7h.mongodb.net/?retryWrites=true&w=majority".format(username, password))
# # url is just an example (your url will be different)
# db = url.test

#general method to connect python and  mongodb cluster
client = pymongo.MongoClient("mongodb+srv://subash032:subash123@subash.k8i7h.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

#Insert some of the data set into the
data = {
    "name" :"Subash",
    "mail id":"suabshselvarajatmcas@gmail.com",
    "Subject":["data science","bigdata","data analytics"]
}

database = client['myinfo'] #creation of database
collection = database["subash"] #create table in mongodb its called as collection(inside collection(tables) we can store the documents(values)
#collection.insert_one(data) #it will insert the one document(values) inside the collection(tables)

#insert the multiple records(dictionaries)

list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]
#collection.insert_many(list_of_records)

collection1 = database["dbkt"]
data1 = {"packetType": "D",
          "data": {"checkEngineLightFlag": "F", "batteryVoltageStableTime": 0, "batteryVoltageStable": "0",
                   "batteryVoltageOff": "12.42", "batteryCrankParamTN": "-0.08", "batteryCrankParamVN": "0.00",
                   "batteryCrankParamTP": "-0.08", "batteryCrankParamVP": "0.00", "batteryCrankParamTT": "-0.00008",
                   "batteryCrankParamV0": "0.00", "batteryVoltageMaxOn": "13.05", "batteryVoltageMinOn": "12.97",
                   "batteryVoltageMaxOff": "12.46", "batteryVoltageMinOff": "12.36", "batteryVoltageOnAverage": "13.02",
                   "engineLoadMax": "84", "engineLoadAverage": "39.98", "rpmMax": "3487", "rpmAverage": "1431.29",
                   "gpsSpeedAverage": "21.99", "vssMax": "53.44", "vssAverage": "23.06", "tcuTemperatureMin": "82.40",
                   "tcuTemperatureMax": "109.40", "tcuTemperatureAverage": "104.87", "coolantMin": "158.00",
                   "coolantMax": "188.60", "coolantAverage": "180.20", "packetStartLocal": 1508143346000,
                   "tripStartLocal": 1508143346000, "milIndicator": "F", "monitorsNotReady": 0, "imei": "60DF5417",
                   "gatewayTs": 1515613306592, "diagnosticTroubleCodeData": [],
                   "diagnosticPidData": [[64768, 47, 100], [64768, 1, 517376], [64800, 1, 262144], [64768, 5, 125]]},
          "header": {"iwrapVer": "1.9.20", "sourceSystem": "CDP", "configVer": "1.1", "oemName": "HUM", "unitType": 0,
                     "cpVer": "7.50.1.9", "igpsVer": "1.3.7", "messageType": "Notification", "pomVer": "1.0",
                     "headerVer": "V6", "timestamp": 0, "deviceType": "InDrive", "visorVer": "1.4.35",
                     "transactionId": "53098471-7787-4160-94b3-cd69dcc70416", "deviceSerialNo": "60DF5417",
                     "subOrganization": "HUM", "organization": "HUM", "imei": "60DF5417", "operation": "Notification"}}
#collection1.insert_one(data1)

#fetch all the data from the colections(tables)
record = collection.find()
for i in record:
    print(i)



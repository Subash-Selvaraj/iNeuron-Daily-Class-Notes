import pymongo
#general method to connect python and  mongodb cluster
client = pymongo.MongoClient("mongodb+srv://subash032:subash123@subash.k8i7h.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

database = client['inventory']
collection = database["table"]
#collection.insert_many(data)

#d = collection.find({'status':'A'})
#d = collection.find({'status':{'$in':['A','P']}}) #get the data either 'A' or 'P'
#d = collection.find({'status':{'$gt':"C"}}) #greter than 'C'
#d = collection.find({'qty':100}) #get the data where qty = 100
#d = collection.find({'qty': {"$gte":75}}) #greter than or equal to(gte)
#=======================and==================================================
#d = collection.find({'item':'sketch pad', 'qty':95}) #find record where item = sketch pad and qty = 95
#d = collection.find({'item':'sketch pad', 'qty':{"$gte":75}}) #find record where item = sketch pad and qty >+75
#=======================or==================================================
#d = collection.find({"$or":[{'item':'sketch pad'},{'qty':{"$gte":75}}]})
#=============================upadte the data's into the existing tables==============================================
#upadte the item column where ever we have value 'canvas' to 'brainstorming'
#collection.update_many({"item":"canvas"},{"$set":{"item":"Brainstorming"}})
#d = collection.find({'item':"Brainstorming"})
#=====================================delete============================
#where every we have value item  = brainstorming delete one record from them
collection.delete_one({"item":'Brainstorming'})
d = collection.find({'item':"Brainstorming"})
for i in d:
     print(i)


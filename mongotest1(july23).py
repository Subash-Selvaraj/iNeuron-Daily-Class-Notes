import pymongo
#general method to connect python and  mongodb cluster
client = pymongo.MongoClient("mongodb+srv://subash032:subash123@subash.k8i7h.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

database = client['myinfo'] #creation of database
collection = database["subash"] #create table in mongodb its called as collection(inside collection(tables) we can store the documents(values)

record = collection.find()
#to get all the data from the collections
# for i in record:
#     print(i)

#get the data where ever we have company name as iNeuron
com_name = collection.find({"companyName":"iNeuron"})
# for i in com_name:
#     print(i)

#get the record where the coursename  value was start's with
course_name = collection.find({"courseOffered":{"$gt" :"E"}}) #"$gt" means greaterthan #the filter is get the courseOffered equal to 'E' or after the 'E' letters
for i in course_name:
    print(i)

import pymongo
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = client['Student']
information = mydb.Studentinfo
#Insert some of the data set into the
data = {
    "name" :"Subash",
    "mail id":"suabshselvarajatmcas@gmail.com",
    "Subject":["data science","bigdata","data analytics"]
}
#information.insert_one(data)

datas = [
{
    "name" :"Subash",
    "mail id":"suabshselvarajatmcas@gmail.com",
    "Subject":["data science","bigdata","data analytics"]
},{
    "name" :"Subash",
    "mail id":"suabshselvarajatmcas@gmail.com",
    "Subject":["data science","bigdata","data analytics"]
},{
    "name" :"Subash",
    "mail id":"suabshselvarajatmcas@gmail.com",
    "Subject":["data science","bigdata","data analytics"]
},{
    "name" :"Subash",
    "mail id":"suabshselvarajatmcas@gmail.com",
    "Subject":["data science","bigdata","data analytics"]
}
]
information.insert_many(datas)

from flask import Flask,jsonify,request
import pymongo
app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://subash032:subash032@subash.k8i7h.mongodb.net/?retryWrites=true&w=majority")
database = client['taskdb']
collection = database['taskcollection']

#create a function to insert a data into the database by using mongo db
@app.route('/insert/mongo',methods=['POST'])
def insert():
    if request.method =='POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify("Successfully inserted")

#create a function to update a data into the database by using mongo db
@app.route('/update/mongo',methods=['POST'])
def update():
    if request.method =='POST':
        name = request.json['name']
        collection.update_one({name:name},{"$set":{name}}) #mistakes
        return jsonify("Successfully updated")

if __name__ == '__main__':
    app.run()
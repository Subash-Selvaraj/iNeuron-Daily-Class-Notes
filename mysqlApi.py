from flask import Flask,request,jsonify
import mysql.connector as conn
app = Flask(__name__)
mydb = conn.connect(host = 'localhost',user='root',passwd='root') #to communicating to the pycharm and mysql system database
cursor = mydb.cursor()
#database creation
cursor.execute('create database if not exists tasksql')
#table creation
cursor.execute("CREATE TABLE if not exists tasksql.mysqltable(name varchar(30) NOT NULL,number int)")

#create function along with annotation to insert a data into sql by using API
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into tasksql.mysqltable  values(%s , %s)", (name, number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))

#create function along with annotation to update a data into sql by using API
@app.route('/update',methods=['POST'])
def update():
    if request.method =='POST':
        get_name = request.json['get_name']
        cursor.execute("Update tasksql.mysqltable set number = number + 500 where name = %s",(get_name,))
        mydb.commit()
        return jsonify("Updated successfully")

#create function along with annotation to delete a data into sql by using API
@app.route('/delete',methods=['POST'])
def delete():
    if request.method=='POST':
        name_del = request.json['name_del']
        cursor.execute("delete from tasksql.mysqltable where name = %s",(name_del,))
        mydb.commit()
        return jsonify("Deleted successfully")

#creata a function to get a data from the table\
@app.route('/load',methods=['POST'])
def fetch_data():
    cursor.execute("select*from tasksql.mysqltable")
    l=[]
    for i in cursor:
        l.append(i)
    return jsonify((str(l)))

if __name__ == '__main__':
    app.run()
from flask import Flask, request, jsonify
app = Flask(__name__)
# 1 . Write a program to insert a record in sql table via api database
# 2.  Write a program to update a record via api
# 3 . Write a program to delete a record via api
# 4 . Write a program to fetch a record via api
# 5 . All the above questions you have to answer for mongo db as well .

# 1 . Write a program to insert a record in sql table via api database
import mysql.connector as connection
mydb = connection.connect(host = 'localhost',user='root',passwd='root',database = 'School') #to communicating to the pycharm and mysql system database
cursor = mydb.cursor()
#database creation
cursor.execute('create database if not exists School')
#table creation
scl_table ='''CREATE TABLE if not exists School_details(
   School_Name CHAR(20) NOT NULL,
   School_Type CHAR(20),
   School_Place CHAR(20),
   School_Rank INT
)'''
cursor.execute(scl_table)

#create function along with annotation to insert a data into sql by using API
@app.route('/insert', methods=['GET', 'POST'])
def insert_data():
    if (request.method == 'POST'):
        a = request.json['School_Name']
        b = request.json['School_Type']
        c = request.json['School_Place']
        d = request.json['School_Rank']
        insrt_table= """Insert into School_details(School_Name,School_Type,School_Place,School_Rank)
                Values(a,b,c,d)"""
        cursor.execute(insrt_table)
        mydb.commit()
        return "Pass"
if __name__ == '__main__':
    app.run()
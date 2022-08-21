import mysql.connector as connection

mydb = connection.connect(host = 'localhost',user='root',passwd='root') #to communicating to the pycharm and mysql system database
#print(mydb)

cursor = mydb.cursor()
#command to create a database
cursor.execute("create database student")

#create a table #student is a data base name and #studentdetails is a table name #(inside all are column names and their data types in the table)
cursor.execute("create table student.studentDetails(studentname varchar(20),studentfathername varchar(20),studentDOB int(15),studentaddress varchar(100))")

cursor.execute("Show databases")
#print(cursor.fetchall())
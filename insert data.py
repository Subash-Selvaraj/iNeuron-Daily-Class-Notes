import mysql.connector as connection
mydb = connection.connect(host = 'localhost',user='root',passwd='root') #to communicating from the pycharm to mysql system database
cursor = mydb.cursor()
s="insert into student.studentDetails values('subash','selvaraj',03042000,'Attur')"
s1 = "insert into student.studentDetails Values('Shalini','Kan',04042000,'Thuraiur')"
cursor.execute(s)
cursor.execute(s1)
mydb.commit() #to commit the changes into the databases
cursor.execute("select * from student.studentDetails")
for i in cursor.fetchall():
    print(i)
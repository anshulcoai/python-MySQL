import mysql.connector

try:
    db=mysql.connector.connect(host='localhost',user='root',password='Anshul123456789@',database='hellosql')
    cur=db.cursor()

    crcreate="""
         create table record1(
         rollno numeric(40),
         sname char(20),
         course char(20),
         fee numeric(40))
         """
    i=cur.execute(crcreate)

    if i is None:
        print("Table created successfully")
    else:
        print("Table not created")

    cur.close()
    db.close()
except mysql.connector.Error as E:
    print("connection not established because:=",E)



import mysql.connector

try:
    db=mysql.connector.connect(host='localhost',user='root',password='Anshul123456789@',database='hellosql')
    cur=db.cursor()

    inrecord="insert into record1 values(100,'Mike','History',8000)"
    
    i=cur.execute("select * from record1")
    db.commit()
    if i is None:
        i=1
    else:
        i=0
    print(i,'row Affected')

    cur.close()
    db.close()
except mysql.connector.Error as E:
    print("Connection not Established Because:=",E)

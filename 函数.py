import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="xiaoshuo"
)
mycursor = mydb.cursor()

sql = "INSERT INTO tongji (name, num) VALUES (%s, %s)"
val = ("Zhiu", "1")
mycursor.execute(sql, val)

mydb.commit()

print("1 条记录已插入, ID:", mycursor.lastrowid)
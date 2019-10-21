import mysql.connector

read_id = open("student_id.txt","r")
write_details = open("student_details.txt","w")
mydb =  mysql.connector.connect(host="localhost", user="root", password="root", auth_plugin="mysql_native_password",database="student_management")
mycursor = mydb.cursor(prepared=True)
data = read_id.readlines()
sql_query = "SELECT * FROM student_details WHERE id = %s"
for i in data:
    mycursor.execute(sql_query, i.strip())
    # print(mycursor.fetchall())
    write_details.write(str(mycursor.fetchall())+"\n")
write_details.close()
read_id.close()


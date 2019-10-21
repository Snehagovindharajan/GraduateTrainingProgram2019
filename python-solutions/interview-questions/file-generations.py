import mysql.connector as m

db = m.connect(host="localhost", user="root", password="root", db="student_management", port="3306", auth_plugin= "mysql_native_password")
cursor = db.cursor()
cursor.execute("select * from student_details;")
res = cursor.fetchall()
print(res)

import unicodedata

li = []
for i in res:
    j = str(i[0]).encode()
    li.append(j)
print(li)

import os

os.chdir('C:\\sneha')
for i in li:
    filename = str(i) + '.txt'
    f = open(filename, 'w')
    f.close()

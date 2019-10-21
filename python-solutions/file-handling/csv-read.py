import csv
# write_csv = open("stu_out.csv", 'w')
# with open("student.csv") as csv_ptr:
#     data = csv.reader(csv_ptr, delimiter=',')
#     # for i in data:
#     #     print(i)
#     data1 = csv.writer(write_csv, delimiter=":")
#     for i in data:
#         data1.writerow(i)

dict_read = open("student.csv","r")
dict_write = open("student_dict.csv","w")
data = csv.DictReader(dict_read)
# for i in data:
#     print(i)
# print(list(data))
fieldnames=["id","name"]
data1 = csv.DictWriter(dict_write,fieldnames=fieldnames)
data1.writeheader()
for i in data:
    data1.writerow(i)
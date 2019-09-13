# how to remove the duplicate character from String
string = input("Enter a String")
list1 = []
for i in string:
    list1.append(i)

for i in list1:
    if list1.count(i) > 1:
        list1.remove(i)

str1 = ''
for i in range(0,len(list1)):
    str1 = str1 + list1[i]
print(str1)

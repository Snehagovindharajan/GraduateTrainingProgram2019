string = input("enter a string")
dict1 = {}
for i in string:
    dict1.update({i: string.count(i)})
print("dictionary : ", dict1)

# dictionary to string
str1 = ''
for j in dict1:
        str1 = str1+j+str(dict1[j])
print("String : ", str1)
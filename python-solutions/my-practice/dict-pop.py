string = input("enter a string")
dict1 = {}
for i in string:
    dict1.update({i: string.count(i)})
print("dictionary : ", dict1)
dict1.pop('c')
print("dictionary : ", dict1)
dict1.popitem()
print("dictionary : ", dict1)
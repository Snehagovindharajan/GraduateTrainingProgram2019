# How to find the maximum occurring character in given String
string = input("enter a string")
dict1 = {}
for i in string:
    dict1.update({i: string.count(i)})
# print("dictionary : ", dict1)
max1 = 0
char = ''
for i,j in dict1.items():
    if j > max1:
        max1 = j
        char = i
print("Max Occurring Char : ", char)
# print("Max Occurring Char : ", max(dict1.values()))

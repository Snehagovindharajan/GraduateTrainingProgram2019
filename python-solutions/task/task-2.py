string = input("enter a string")
str1 = ''
for i in string:
    str1 = str1 + i + str(string.count(i))
print(str1)

# reverse of a string
name = input("Enter a String")
str1 = name[::-1]
print("Reverse of a string : ", str1)

str2 = ''
for i in range(len(name) - 1, -1, -1):
    str2 = str2 + name[i]
print("Reverse of string : ", str2)




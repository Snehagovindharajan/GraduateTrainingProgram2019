# 5: Convert the string as below.
# input : abcDEwQ
# output: ABCdeWq

str1 = input("Enter a string")
str2 = ""
for i in str1:
    if i.isupper():
        str2 = str2 + i.lower()
    elif i.islower():
        str2 = str2 + i.upper()
print(str2)
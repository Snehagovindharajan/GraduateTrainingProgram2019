# How do you print duplicate characters from a string?

name = input("Enter a string")
print("duplicate characters")
dict1 = {}
for i in name:
    cnt = name.count(i)
    if (cnt > 1):
        dict1.update({i: cnt})
print(dict1)

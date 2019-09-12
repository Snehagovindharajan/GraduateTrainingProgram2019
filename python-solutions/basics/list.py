string = input("Enter a string")
# list1=list(string)
# print(i*2)
# to print each char twice
list1 = []
for i in string:
    list1.extend(i * 2)
print(list1)

# print the char only twice
# example 1
for j in list1:
    if list1.count(j) > 2:
        for l in range(0, list1.count(j) - 2):
            list1.remove(j)
print(list1)
# example 2
list2 = []
for k in string:
    if k not in list2:
        list2.extend(list(k * 2))
print(list2)

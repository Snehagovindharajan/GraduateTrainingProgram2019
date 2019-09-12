
# insert from keyboard
range1 = int(input("enter a limit"))
lst = []
for i in range(range1):
    a = int(input("enter a number"))
    lst.insert(i, a)
print(lst)

# separate even and odd numbers
list1 = []
list2 = []
for i in range(1,11):
    if i % 2 == 0:
        list1.append(i)
    else:
        list2.append(i)
print(list1)
print(list2)


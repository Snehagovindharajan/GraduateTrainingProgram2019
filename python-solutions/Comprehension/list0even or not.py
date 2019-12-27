lst = [i for i in range(1,50) if i % 2 == 0 and i != 2]
print(lst)

lst1 = [i for i in range(1,50) if i % 3 == 0]
print(lst1)

lst2 = []
for i in range(1,100):
    if i % 3 == 0:
        lst2.append(3)
    elif i % 5 == 0:
        lst2.append(5)
    else:
        lst2.append(i)
print(lst2)
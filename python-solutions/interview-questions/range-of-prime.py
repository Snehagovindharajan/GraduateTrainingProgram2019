prime_range = 17
list1 = []
for i in range(2,prime_range):
    for j in range(2,i):
        if i % j == 0 and i != j:
            break
        else:
            if i not in list1:
                list1.append(i)
print(list1)
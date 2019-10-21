S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S1 = [1, 2, 3, 4, 5, 6, 7, 8]
unique_list = []
unique_list1 = []
for i in S:
    if i not in S1:
        unique_list.append(i)
for i in S1:
    if i not in S:
        unique_list1.append(i)

print(unique_list)
print(unique_list1)
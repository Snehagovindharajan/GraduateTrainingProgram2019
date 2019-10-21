original_list = [[1], [1, 1]]

for i in range(2, 7):
    j = original_list[i - 1]
    count = 1
    iter_list = [1, 1]
    for key in range(0, len(j)):
        sum = 0
        for keey in range(key + 1, len(j)):
            sum = j[key] + j[keey]
            iter_list.insert(count, sum)
            count = count + 1
            break
    original_list.append(iter_list)
# print(original_list)
for i in original_list:
    for j in i:
        # str1 = str(j)
        # print(str1.center(1, ' '), end=" ")
        print(j, end=" ")
    print("\n")

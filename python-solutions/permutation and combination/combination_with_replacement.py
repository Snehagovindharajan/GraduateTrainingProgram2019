from itertools import combinations_with_replacement

# model 1
# list1 = [i for i in input().split(" ")]
# string1 = list1[0]
# size = int(list1[1])
# string = sorted(string1)
# result = []
# for i in range(1, size + 1):
#     result.append(list(combinations_with_replacement(string, i)))
# print(result)
# for i in result:
#     list2 = []
#     for j in i:
#         print(''.join(j))

# model 2
# list1 = [i for i in input().split(" ")]
# string1 = list1[0]
# size = int(list1[1])
# string = sorted(string1)
# result = combinations_with_replacement(string,size)
# for i in result:
#     print(''.join(i))

# model 3
list1 = [i for i in input().split(" ")]
string1 = list1[0]
size = int(list1[1])
string = sorted(string1)
for i in range(1, size + 1):
    result = combinations_with_replacement(string, i)
    for j in result:
        print(''.join(j))

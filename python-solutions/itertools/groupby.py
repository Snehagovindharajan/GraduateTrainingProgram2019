from itertools import groupby

string = "aaaabbbbbaachhhvvd"
string_list = list(string)
# print(string_list)
for key, group in groupby(string, lambda x : x):
    result = (len(list(group)), key)
    print(result, end=" ")


# string = "1"
# string_list = list(string)
# list1 = []
# for key, group in groupby(string_list, lambda x: x):
#     list2 = []
#     for element in group:
#         list2.append(element)
#     list1.append(list2)
# for i in list1:
#     result = [i.count(i[0]), int(i[0])]
#     print(tuple(result), end=" ")

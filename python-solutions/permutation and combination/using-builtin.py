# How many words can be formed by using 3 letters from the word “DELHI” ?
from itertools import permutations

# string = "DELHI"
# # string_list = list(string)
# # print(string_list)
# result = permutations(string,3)
# for i in result:
#     print("".join(i))

#  How many number greater than thousand can be formed from the digits 0, 1, 2, 3, 4 without repetation ?

# num_list = [0, 1, 2, 3, 4]
# final_list = []
# final_list1 = []
# result = permutations(num_list, len(num_list))
# for i in result:
#     str1 = ""
#     for j in i:
#         str1 = str1 + str(j)
#     final_list.append(str1)
# # print(final_list)
# for i in final_list:
#     if int(i) > 10000:
#         final_list1.append(i)
# print(len(final_list1))

# with repetition
import itertools
x = [1, 2, 3, 4, 5, 6]
result = [p for p in itertools.product(x, repeat=2)]
print(len(result))
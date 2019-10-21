from itertools import combinations

length = 4
string = ['a', 'a', 'c', 'd']
index_list = [i for i in range(1, length + 1)]
indices = 2
result = combinations(index_list, 2)
# for i in result:
#     print(i)
a_index = [key + 1 for key, value in enumerate(string) if value == 'a']
# print(a_index)
set1 = set([])
for i in result:
    for j in i:
        if j in a_index:
            set1.update([i])
# print(set1)
probability = int(len(set1))/int(len(result))
print(probability)
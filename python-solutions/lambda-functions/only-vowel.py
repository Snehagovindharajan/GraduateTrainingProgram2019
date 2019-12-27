# vowel should be removed from a list using lambda function
from functools import reduce

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
consonant = list(filter(lambda x: x not in ('a', 'e', 'i', 'o', 'u'), lst))
print(consonant)

string = 'accenture'
count = list(map(lambda cnt: cnt + '1', string))
str1 = ''
for i in count:
    str1 = str1 + i
print(str1)

lst1 = [1, 2, 3, 4]
multiply = reduce(lambda one, two: one * two, lst1)
print(multiply)

emp_id = '11729554'
answer = list(map(lambda id: id + id, emp_id))
print(answer)
str2 = ''
for i in answer:
    str2 = str2 + i
print(str2)
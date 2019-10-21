from itertools import combinations,combinations_with_replacement

# without repetition
string = "DELHI"
# list_string = list(string)
result = combinations(string,5)
for i in result:
    print(''.join(i))

# with repetition
string = "DELHI"
result = combinations_with_replacement(string,5)
for i in result:
    print(''.join(i))
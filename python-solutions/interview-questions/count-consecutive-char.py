# s = 'aappaaggglllgg'
# str1 = ""
# for i in s:
#     if i not in str1:
#         str1 = str1 + str(s.count(i)) + i
# print(str1)

from itertools import groupby

# s = 'aaaakkkkrrrriiioogftrrrmmkkkpp'
# str2 = ""
# for key, value in groupby(s, lambda x: x):
#     print(len(list(value)))
#     str2 = str2 + str(len(list(value))) + key
# print(str2)

# s = 'aaaakkkkrrrriiioogftrrrmmkkkpp'
# c = 1
# o = ""
# for i in range(1, len(s)):
#     if s[i - 1] == s[i]:
#         c += 1
#     else:
#         o += (s[i - 1] + str(c) + "-")
#         c = 1
# o += s[i]+str(c)
# print(o)

# max of occurance
s = 'aaaakkkkrrrriiioogftrrrmmkkkpp'
str2 = ""
max_val = 0
key1 = ''
value1 = []
for key, value in groupby(s, lambda x: x):
    v = len(list(value))
    # print(key, list(value), len(list(value)))
    if max_val < v:
        print(max_val)
        max_val = v
        key1 = key
        value1 = value
str2 = str(max_val) + key1
# print(str2)
#
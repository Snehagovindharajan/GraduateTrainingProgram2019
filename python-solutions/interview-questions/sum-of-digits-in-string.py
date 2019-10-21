s = '2 sum 34 the  567 integers 6756 in  the  67 given  88 string 5 m'

# method 1
sum = 0
for i in s:
    if i.isdigit():
        sum = sum + int(i)
print(sum)

# method 2
import re

digit = re.findall("\d", s)
sum = 0
for i in digit:
    sum = sum + int(i)
print(sum)

op = 'asdfghjklpoiuytrewq'
str1 = ""
for i in op:
    if i in 'aeiou':
        continue
    else:
        str1 = str1 + i
print(str1)

str1 = ""
for i in op:
    if i not in 'aeiou':
        str1 = str1 + i
print(str1)
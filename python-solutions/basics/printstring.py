#printing string normaly and using index
name = "welcome"
for i in name:
     print(i)
print(name[2])

#reverse of string using slicing
print(name[::-1])

#length of string
print(len(name))

count = 0
for j in name:
    count = count + 1
print(count)

#count of 'e'
print(name.count('e'))

count1 = 0
for j in name:
    if (j == 'e'):
        count1 = count1 + 1
print(count1)

#split string into wel and come
count2 = 0
name1 = ''
name2 = ''
for k in name:
    if (count2 > 2):
        name2 = name2 + k
    else:
        name1 = name1 + k
        count2 = count2 + 1
print(name1)
print(name2)


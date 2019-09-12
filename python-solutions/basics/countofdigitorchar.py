# count of digit and char
# example1
list3 = ['1', 'a']
count1 = 0
count2 = 0
for i in list3:
    if 97 <= ord(i) <= 122:
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print(count1)
print(count2)

# example2
list4 = ['2', 'a']
count1 = 0
count2 = 0
for i in list4:
    if i.isdigit():
        count1 = count1 + 1
        # print(i)
    elif i.isalpha():
        count2 = count2 + 1
        # print(i)
print(count1)
print(count2)

# example3
list1 = ['1', 'z']
count1 = 0
count2 = 0
for i in list1:
    if 'z' >= i >= 'a':
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print(count1)
print(count2)

# example4
list2 = [10,'s']
count1 = 0
count2 = 0
for i in list2:
    if type(i)==int:
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print(count1)
print(count2)
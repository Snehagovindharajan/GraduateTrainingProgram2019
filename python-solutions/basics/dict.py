# create a dict from a list and containing a list if there are duplicate keys
# common
list3 = ['five', 5, 'six', 6, 'seven', 7, 'seven', 8, 'nine', 9]
list1 = []
list2 = []
for i in list3:
    if type(i) == int:
        list1.append(i)
    else:
        list2.append(i)

# example1 prints only distinct keys
dict1 = {}
for i in range(0, len(list1)):
    dict1[list2[i]] = list1[i]
print(dict1)

# example2
dict2 = {}
for j in range(0, len(list1)):
    if list2[j] in dict2:
        dict2.update({list2[j]: [list1[j - 1], list1[j]]})
    else:
        dict2.update({list2[j]: list1[j]})
print(dict2)

# example3
dict3 = {}
for k in range(0,len(list3),2):
    for l in range(1,len(list3),2):
        if(list3[l-1] == list3[k]):
            if list3[k] not in dict3:
                dict3.update({list3[k]:list3[l]})
            else:
                dict3.update({list3[k]:[list3[l-2],list3[l]]})
print(dict3)
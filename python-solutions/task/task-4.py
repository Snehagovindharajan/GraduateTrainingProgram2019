lst = ['five plus three', 'seven minus two', 'two plus eight minus five', 'eight divide four']
dct = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'plus': '+', 'minus': '-', 'divide': '/'}
lst1 = []
for i in lst:
    string = i.split(" ")
    str2 = ''
    for j in string:
        if j in dct:
            str2 = str2 + j.replace(j, str(dct[j]))
    lst1.append(str2)
print(lst1)
lst2=[]
for k in lst1:
    lst2.append(eval(k))
print(lst2)
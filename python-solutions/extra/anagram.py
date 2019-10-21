list1 = ['add', 'listen', 'adcd', 'silent', 'sneha', 'acdd', 'dad', 'jayasree']
dict1 = {}
count = 0
for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if sorted(list1[i]) == sorted(list1[j]):
            dict1.update({list1[i]:list1[j]})
print(dict1)

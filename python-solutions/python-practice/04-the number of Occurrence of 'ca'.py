# 4: The string abcabcabc........ goes till 1111 . print the number of Occurrence of 'ca'

str1 = ''
for i in range(0,1111):
    if i % 3 == 0:
        str1 = str1 + 'a'
    if i % 3 == 1:
        str1 = str1 + 'b'
    if i % 3 == 2:
        str1 = str1 + 'c'
count = 0
for i in range(len(str1)):
    if str1[i] == 'c' and str1[i+1] == 'a':
            count = count + 1
print(count)
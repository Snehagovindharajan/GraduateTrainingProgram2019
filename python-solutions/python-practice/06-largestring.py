# 6: Find the ordered longest alphabetical sequence.
# abccdefabcdefae

string = "abccdefabcdefae"
str1 = ''
list1 = []
for i in range(0,len(string)-1):
    if ord(string[i]) == ord(string[i+1])-1:
        str1 = str1 + string[i]
    else:
        str1 = str1 + string[i]
        list1.append(str1)
        str1 = ''
list1.append(string[i])
print(list1)
maxi = 0
max_val = ''
for i in list1:
    if len(i) > maxi:
        max_val = i
        maxi = len(i)
print(max_val)
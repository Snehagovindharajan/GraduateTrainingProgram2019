str1 = 'accd'
str2 = 'acdd'
count = 0
if (len(str1) == len(str2)):
    for i in range(0,len(str1)):
        if str1[i] in str2 and str2[i] in str1:
            count = count + 1

if count == len(str1):
    print("anagram")
else:
    print("Not")
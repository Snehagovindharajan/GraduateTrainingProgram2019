# find anagram for two given string ex. add, dad --> anagram

str1 = input("Enter a string : ")
str2 = input("Enter a string : ")
lst = []
lst1 = []
for i in str1:
    lst.append(i)
for i in str2:
    lst1.append(i)
lst.sort()
lst1.sort()

if lst == lst1:
    print("anagram")
else:
    print("Not")
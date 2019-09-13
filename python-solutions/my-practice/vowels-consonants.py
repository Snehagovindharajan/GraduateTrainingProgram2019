# How do you count a number of vowels and consonants in a given string
name = input("Enter a string")
list1 = []
list2 = []
for i in name:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        list1.append(i)
    else:
        list2.append(i)

dict1 = {'vowels':len(list1),'consonants':len(list2)}
print("count : ",dict1)
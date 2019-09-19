# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.


def is_anagram(str1, str2):
    lst = []
    lst1 = []
    for i in str1:
        lst.append(i)
    for i in str2:
        lst1.append(i)
    lst.sort()
    lst1.sort()

    if lst == lst1:
        return True
    else:
        return False


str1 = input("Enter a string : ")
str2 = input("Enter a string : ")
result = is_anagram(str1, str2)
if result:
    print("anagram")
else:
    print("Not a anagram")
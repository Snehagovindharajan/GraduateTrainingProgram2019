# anagram : sample inputs : tear, rate ; Find if these words are anagram or not. Program should accept two inputs
# from user.

str1 = input("Enter a string")
str2 = input("Enter another string")
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an anagram")
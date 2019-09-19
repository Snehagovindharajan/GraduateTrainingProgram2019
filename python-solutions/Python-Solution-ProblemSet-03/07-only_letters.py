#  Write a function named using_only() that takes a word and a string of letters, and
# that returns True if the word contains only letters in the list. Can you make a sentence using only
# the letters acefhlo? Other than "Hoe alfalfa?"
string = input("Enter a string to check")
shld_contain = input("Enter a string")
lst = [i for i in string if i in shld_contain]
str2 = ''
for i in lst:
    str2 = str2 + i
print(str2)
if str2 == string:
    print("only letters")
else:
    print("No")
# 9: "There are 26 alphabets in English out of which 5 are vowels and 21 are consonants"
# Count the sum of numbers in the above statement using regular expression
import re
string = "There are 26 alphabets in English out of which 5 are vowels and 21 are consonants"
str1 = re.findall('[0-9]+',string)
sum = 0
for i in str1:
    sum = sum + int(i)
print(sum)
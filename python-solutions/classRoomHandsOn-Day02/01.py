# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
#  Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

string = "Hello world!"
upper = 0
lower = 0
for i in string:
    if i.isalpha():
        if i == i.upper():
            upper = upper + 1
        if i == i.lower():
            lower = lower + 1
dict1 = {'UPPER':upper,'LOWER':lower}
print(dict1)
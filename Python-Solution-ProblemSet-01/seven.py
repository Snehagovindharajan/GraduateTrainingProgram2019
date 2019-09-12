# Write a function isIn() that accepts two strings as arguments
# and returns True if either string occurs anywhere in the other, and False
# otherwise. Hint: you might want to use the built-in str operation in.

def Isin(str_one,str_two):
    if str_one in str_two or str_two in str_one:
        return True
    else:
        return False
    #print(str_one,str_two)


str_one = input("Enter a name")
str_two = input("Enter a name")
if(Isin(str_one, str_two)):
    print("string contains other string")
else:
    print("no substring")

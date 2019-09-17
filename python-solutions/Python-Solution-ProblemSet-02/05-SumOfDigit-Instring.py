# Implement a function that meets the specification below. Use a try-except block.
# ```python
# def sumDigits(s):
# 	"""Assumes s is a string
# 	Returns the sum of the decimal digits in s
# 	For example, if s is 'a2b3c' it returns 5"""
# ```

def sumDigits(s):
    sum = 0
    flag = 0
    for i in string:
        if i.isdigit():
            sum = sum + int(i)
            flag = 1
    return sum, flag


try:
    string = input("Enter a string")
    result, flag = sumDigits(string)
    if flag == 0:
        raise Exception
    else:
        print("Sum Of Digits : ", result)
except Exception:
    print("No digits in the string")

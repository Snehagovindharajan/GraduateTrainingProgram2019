# Implement a function that meets the specification below. Use a try-except block.
# ```python
# def sumDigits(s):
# 	"""Assumes s is a string
# 	Returns the sum of the decimal digits in s
# 	For example, if s is 'a2b3c' it returns 5"""
# ```

def sumDigits(s):
    sum = 0
    for i in string:
        if i.isdigit():
            sum = sum + int(i)
    return sum


string = input("Enter a string")
result = sumDigits(string)
print("Sum Of Digits : ", result)

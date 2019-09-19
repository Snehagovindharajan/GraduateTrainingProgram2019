# A string slice can take a third index that specifies the "step size;" that is, the number
# of spaces between successive characters. A step size of 2 means every other character; 3 means every
# third, etc.
# ```python
# >>> fruit = 'banana'
# >>> fruit[0:5:2]
# 'bnn'
# ```
string = input("Enter a string")
print(string[0:len(string):2])
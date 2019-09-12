#  Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# delimiter = '.'
# For each of the following expressions, write the value of the expression and the type (of the value of
# the expression).
#
# ```python
# >>> width/2
# >>> width/2.0
# >>> height/3
# >>> 1 + 2 * 5
# >>> delimiter * 5
# Use the Python interpreter to check your answers

width = int(input("width = "))
height = float(input("height = "))
delimiter = input("delimeter = ")

print("width/2 : ", width/2)
print("width/2.0 : ", width/2.0)
print("height/3 : ", height/3)
print("delimeter * 5 : ", delimiter * 5)

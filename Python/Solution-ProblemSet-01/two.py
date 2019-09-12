# Python provides a built-in function called len that returns the length of a string, so
# the value of len('Cigna') is 5. Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
#
# ```python
# >>> right_justify('Cigna')
# 																	 Cigna

# example 1
def right_justify(string):
    for i in range(1, 70-len(string)):
        print(end=" ")
    print(string)


name = input("Enter a string")
right_justify(name)


# example 2
def right_justify1(string):
    print(string.rjust(70-len(string)))


name = input("Enter a string")
right_justify1(name)

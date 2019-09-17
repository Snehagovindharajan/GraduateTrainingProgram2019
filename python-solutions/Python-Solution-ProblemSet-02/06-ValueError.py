# Implement a function that satisfies the specification. Use a try-except block.
# ```python
# def findAnEven(l):
# 	"""Assumes l is a list of integers
# 	Returns the first even number in l
# 	Raises ValueError if l does not contain an even number"""
# ```

def even(list1):
    count = 0
    for i in list1:
        if int(i) % 2 == 0:
            count = count + 1
            break
    if count == 1:
        return i
    else:
        return -1


try:
    range1 = int(input("Enter range"))
    list1 = []
    for i in range(0, range1):
        value = input("enter values")
        list1.append(value)
    num = even(list1)
    if num != -1:
        print(num)
    else:
        raise ValueError
except ValueError:
    print("No Even Number")

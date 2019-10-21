# Type error
try:
    value = input("enter number")
    c = value / 2
    print(c)
except TypeError as e:
    print(e)

# Name error

try:
    value = 1
    print(a)
except NameError as e:
    print(e)

# index error

try:
    list1 = [1, 2, 3, 4, 5, 6]
    print(list1[9])
except IndexError as e:
    print(e)

# key error

try:
    dict1 = {1: 'one', 2: 'two', 3: 'three'}
    print(dict1[4])
except KeyError as e:
    print("Key Error: ", e)

# Zerodivision error

try:
    a = 0
    b = 1
    c = b / a
    print(c)
except ZeroDivisionError as e:
    print(e)

# Value error
try:
    ans = int(input("enter"))
    print(ans)
except ValueError as e:
    print(e)

# File Not Found Error
try:
    read_ptr = open("hello.txt","r")
    data = read_ptr.read()
    print(data)
except FileNotFoundError as e:
    print(e)

class NegativeError(Exception):
    def __init__(self):
        print("Negative error")

try:
    a = int(input("enter"))
    if a < 0 :
        raise NegativeError
    else:
        print("OK")
except NegativeError as e:
    print(e)
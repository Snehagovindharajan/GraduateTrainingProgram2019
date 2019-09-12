# Write a program that asks the user to enter an integer and
# prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.

# example1
integer = int(input("Enter a number"))

for i in range(1, 6):
    for j in range(1, 1000):
        value = pow(j, i)
        if value == integer:
            print("root is : ", j, "power is : ", i)

# example2
integer = int(input("Enter a number"))

for i in range(1, 6):
    for j in range(1, 1000):
        value = j ** i
        if value == integer:
            print("root is : ", j, "power is : ", i)

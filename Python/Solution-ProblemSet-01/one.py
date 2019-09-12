#  Write a program that examines three variables—x, y, and z—
# and prints the largest odd number among them. If none of them are odd, it
# should print a message to that effect.

x = int(input("Enter a number"))
y = int(input("Enter a number"))
z = int(input("Enter a number"))

# example1
list1 = []
if x % 2 != 0:
    list1.append(x)
if y % 2 != 0:
    list1.append(y)
if z % 2 != 0:
    list1.append(z)
if len(list1) != 0:
    print("Max Odd Number : ",max(list1))
else:
    print("No Odd Number")

# example2
if x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
    print("Max Odd number : ",max(x,y,z))
elif x % 2 != 0 and y % 2 != 0:
    print("Max Odd number : ", max(x, y))
elif x % 2 != 0 and z % 2 != 0:
    print("Max Odd number : ", max(x, z))
elif z % 2 != 0 and y % 2 != 0:
    print("Max Odd number : ", max(z, y))
elif x % 2 != 0:
    print("Max Odd number : ",x)
elif y % 2 != 0:
    print("Max Odd number : ",y)
elif z % 2 != 0:
    print("Max Odd number : ",z)
else:
    print("No Odd Number")
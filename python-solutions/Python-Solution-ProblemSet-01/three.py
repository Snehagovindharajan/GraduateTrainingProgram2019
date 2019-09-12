# Write a program that asks the user to input 10 integers, and
# then prints the largest odd number that was entered. If no odd number was
# entered, it should print a message to that effect.

list1 = []
for i in range(0,10):
    a = int(input("enter a number"))
    if a % 2 != 0:
        list1.append(a)

if len(list1) != 0:
    print("Max of list : ",max(list1))
else:
    print("No Odd Numbers")
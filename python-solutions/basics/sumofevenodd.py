a = int(input("enter a number"))
b = int(input("enter an other number"))
even = 0
odd = 0
for i in range(a,b):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print("Even Sum " , even)
print("Even Sum " , odd)
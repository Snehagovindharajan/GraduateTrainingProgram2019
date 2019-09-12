# basic for with +ve step value
for i in range(1, 11):
    print(i)

for j in range(0, 11, -1):
    print(j)

a = int(input("enter a number"))
b = int(input("enter an other number"))
for k in range(a, b):
    print("value : ", k)

# limit the loop using break
for i in range(1, 6):
    if (i == 4):
        print("Limit exceeded")
        break
    else:
        print(i)
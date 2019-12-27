# prime or not
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
list1 = []
for i in range(num1,num2):
    for j in range(2,i):
        if i != j and i % j == 0:
            break
        else:
            if i not in list1:
                list1.append(i)
print(list1)
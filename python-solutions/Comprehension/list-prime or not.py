num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
list1 = [i for i in range(num1, num2) for j in range(2, i) if i != j and i % j == 0]
list2 = [j for j in range(num1, num2) if j not in list1]
print(list2)
# Write a Python program to perform sum of three given integers. However, if any of the two values are equal then sum
# will be zero (eg : 2+1+1 = 0)

no1 = int(input("Enter a number"))
no2 = int(input("Enter a number"))
no3 = int(input("Enter a number"))
sum = 0
if no1 == no2 or no2 == no3 or no3 == no1 :
    sum = 0
else:
    sum = no1+no2+no3
print(sum)
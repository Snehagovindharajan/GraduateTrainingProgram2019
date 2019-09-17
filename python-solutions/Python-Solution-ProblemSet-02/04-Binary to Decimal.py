# Write a program that computes the decimal equivalent of the binary number
# 10011?
num = int(input("Enter a number"))
temp = num
i = 0
decimal = 0
while (temp > 0):
    remainder = temp % 10
    decimal = remainder * pow(2,i) + decimal
    temp = temp // 10
    i = i + 1
print(decimal)
# 12: find if the below numbers are Armstrong number
# a: 153
# b:1634
# c: 876

num = int(input("Enter a number"))
length = len(str(num))
temp = num
power = 0
while num > 0:
    reminder = num % 10
    power = power + pow(reminder,length)
    num = num // 10
if temp == power:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
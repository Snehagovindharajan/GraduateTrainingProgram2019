string = input("Enter a String")
str1 = ''
for i in range(len(string) - 1, -1, -1):
    str1 = str1 + string[i]
if string == str1:
    print("Palindrome")
else:
    print("Not a Palindrome")

# palindrome of number
number = int(input("Enter a number"))
str2 = ''
str_num = str(number)
for i in range(len(str_num) - 1, -1, -1):
    str2 = str2 + str_num[i]
if str_num == str2:
    print("Palindrome")
else:
    print("Not a Palindrome")

# palindrome
number = int(input("Enter a number"))
temp = number
remainder = 0
while temp > 0:
    num = temp % 10
    remainder = remainder * 10 + num
    temp = temp // 10
if remainder == number:
    print("Palindrome")
else:
    print("Not a Palindrome")

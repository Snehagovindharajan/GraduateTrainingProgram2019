#  A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
# function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
# you will have to think about the base case.

def is_Power(num1, num2):
    count  = 0
    if num1 % num2 == 0:
        for i in range(1,50):
            if(pow(num2,i) == num1):
                count = count + 1
                break
    if count > 0:
        return True
    else:
        return False


num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
answer = is_Power(num1,num2)
if(answer):
    print("Yes")
else:
    print("No")

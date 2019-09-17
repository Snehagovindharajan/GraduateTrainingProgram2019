# Observe the following function definitions. They Calculate the Factorial as per the Mathematical
# definition 1! = 1
# 		  (n + 1)! = (n + 1) * n!
# Implement factI(n) as an Iterative Implementation & factR(n) as a Recursive Implementation
# ```python
# def factI(n):
# 	"""Assumes that n is an int > 0
# 	Returns n!
# 	Uses Iterative Implementation"""
#
# def factR(n):
# 	"""Assumes that n is an int > 0
# 	Returns n!
# 	Uses Recursive Implementation"""
# ```
def factorial_Recurcive(num1):
    if num1 == 0:
        return 1
    return num1 * factorial_Recurcive(num1 - 1)

def factorial_Iterative(num1):
    answer = 1
    for i in range(1,num1+1):
        answer = answer * i
    return answer


num1 = int(input("Enter a number"))

result_R = factorial_Recurcive(num1)
print("Factorial : ",result)


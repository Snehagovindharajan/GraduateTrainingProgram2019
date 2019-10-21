def factorial(fact_num):
    fact = 1
    for i in range(1, fact_num + 1):
        fact = fact * i
    print(fact)


factorial(5)


def factorial_recursion(num):
    if num == 1:
        return 1
    else:
        return num * factorial_recursion(num - 1)


num = 5
print(factorial_recursion(num))

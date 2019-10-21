def fibonacci(fib_num):
    f1 = 0
    f2 = 1
    print(f1, end=",")
    print(f2, end=",")
    for i in range(0, fib_num):
        f3 = f1 + f2
        print(f3, end=",")
        f1 = f2
        f2 = f3


fibonacci(15)


def fibonacci_recursion(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


num = 5
for i in range(num):
    print(fibonacci_recursion(i))

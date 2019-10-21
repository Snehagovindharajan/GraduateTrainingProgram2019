def binary_to_decimal(num):
    count = 0
    digit = 0
    while num > 0:
        reminder = num % 10
        digit = reminder * pow(2, count) + digit
        num = num // 10
        count = count + 1
    print(digit)


binary_to_decimal(1010)

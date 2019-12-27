def sum(a, b):
    add = a + b
    return add


def addition():
    ans = sum(2, 5)
    if ans < 10:
        ans = ans + 1
    return ans


result = addition()
print("answer : ", result)

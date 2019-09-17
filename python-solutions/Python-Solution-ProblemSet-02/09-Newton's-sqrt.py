#  One way of computing square roots is Newton’s method. Suppose that you
# want to know the square root of a. If you start with almost any estimate, x, you can compute
# a better estimate with the following formula:
# y = (x + a/x)/2 For example, if a is 4 and x is 3:
#
# ```python
# >>> a = 4.0
# >>> x = 3.0
# >>> y = (x + a/x) / 2
# >>> print y
# 2.16666666667

import math





def math_sqrt(num1):
    lst2 = []
    for i in num1:
        msqrt = math.sqrt(i)
        lst2.append(msqrt)
    return lst2


def test_square_root(nsqrt, msqrt):
    lst3 = []
    for i in range(0, len(nsqrt)):
        difference = nsqrt[i] - msqrt[i]
        lst3.append(difference)
    return lst3


num1 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
nsqrt = newton_sqrt(num1)
msqrt = math_sqrt(num1)
diff = test_square_root(nsqrt, msqrt)
print("Number  | Newtons sqrt  | math.sqrt  | Difference");
print("--------|---------------|------------|--------------")
for i in range(0, len(nsqrt)):
    print(num1[i], "    |", nsqrt[i], "          |", msqrt[i], "       |", diff[i])

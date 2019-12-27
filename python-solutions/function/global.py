x = 12
a = 10
def func():
    global x
    x = x + 2
    print(a)
    print(" x value : ",x)
func()
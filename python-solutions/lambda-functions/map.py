lst = [1, 2, 3, 4]
multiply = list(map(lambda x: x < 0, lst))
print(multiply)
pos = list(filter(lambda a: a > 0, lst))
print(pos)

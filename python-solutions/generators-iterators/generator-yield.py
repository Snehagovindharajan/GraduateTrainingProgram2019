# to create generator using yield
def lst_generator(lst):
    for i in lst:
        yield (i, i * 2)
    # for i in lst:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = lst_generator(lst)
for i in result:
    print(i)

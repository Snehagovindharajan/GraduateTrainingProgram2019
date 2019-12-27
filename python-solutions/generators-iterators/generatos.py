# to create generator using ()
generator = (i for i in range(1, 11))
print(generator)  # <generator object <genexpr> at 0x01320FB0>
print(generator.__next__())  # 1
print(next(generator))  # 2
for i in generator:
    print(i)  # prints from 3 t0 9
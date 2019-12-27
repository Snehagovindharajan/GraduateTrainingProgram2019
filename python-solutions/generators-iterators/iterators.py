lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iter_lst = iter(lst)
print(iter_lst)  # <list_iterator object at 0x032EDE90>
print(iter_lst.__next__())  # 1
print(next(iter_lst))  # 2
for i in iter_lst:
    print(i)  # prints from 3 t0 9

string = "accenture"
iter_string = iter(string)
print(iter_string)  # <list_iterator object at 0x032EDE90>
print(iter_string.__next__())  # a
print(next(iter_string))  # c
for i in iter_string:
    print(i)  # prints from c c e n t u r e

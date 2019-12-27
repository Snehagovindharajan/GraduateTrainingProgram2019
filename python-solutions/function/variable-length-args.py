def calculator(operation, *args):
    if operation == 'add':
        add = 0
        for i in args:
            add = add + i
        print("add : ", add)
    if operation == 'sub':
        sub = 0
        for i in args:
            sub = i - sub
        print("sub : ", sub)
    print("List of arguments : ",args)


calculator("add", 2, 3)
calculator("sub", 7, 8, -16)
calculator("add", 2, 3, -8)
calculator("sub", 7, 8)


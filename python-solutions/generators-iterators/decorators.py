def a(func):
    def ball():
        print("something")
        func()
        print("end")

    return ball()


# @a
def b():
    print("b class")


decor = a(b)  # is equal to @a

a = 0


def Foo():
    global a
    if a == 3:
        a = 3
    print(a)


Foo()

a = "hello"


def change(x):
    if x:
        a = "we juest change a"  # variable assignment

    print(a)


# UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
change(False)

def my_addtion(a, b):
    # doctring
    '''
    This function takes two arguments and returns the sum of them.
    '''
    return a+b
    print("Hello World")


# help(my_addtion)
# print(my_addtion.__doc__)
# print(my_addtion.__annotations__)
# print(my_addtion.__code__)
# print(my_addtion.__name__)
# print(my_addtion.__module__)
# print(my_addtion.__defaults__)

a = my_addtion(1, 1)
b = my_addtion(2, 2)
print(a + b)


def my_addtion_loop(a, b):
    for i in range(a):
        for j in range(b):
            if i == 3 and j == 3:
                return
            print(i, j)


my_addtion_loop(5, 5)

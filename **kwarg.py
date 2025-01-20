def my_function(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")


my_function(first='a', second='b', third='c')


def my_function2(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like to eat {} {}".format(args[0], kwargs['food']))


my_function2(4, 2, 3, food='pizza', drink='beer')
# Output:
# (1, 2, 3)
# {'food': 'pizza', 'drink': 'beer'}
# I would like to eat 1 pizza

# 1.normal arguments
# 2. default arguments
# 3. *args
# 4. **kwargs


def func(p1, p2, p3=3, *args, **kwargs):
    print("-----------------")
    print(p1, p2, p3, args, kwargs)
    print(args[0], args[len(args)-1])


func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, a=1, b=2, c=3)
func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, a=1, b=2, c=3, d=4, e=5)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 測試函數
print_kwargs(name="Alice", age=30, city="New York")

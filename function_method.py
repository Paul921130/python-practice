my_list = [1, 2, 3, 4, 5]
my_list.insert(6, 2)
x = 0


def hello():
    x = 10
    print("Hello, World!")
    return x


# function execution, invokation
hello()
print(hello)
print(type(hello))
print(x)


def addition(a, b):
    return a+b


x = addition(1, 30)
print(x)

# global variables, local variables
s = 5  # global variable


def f1():
    x = 2  # local variable
    y = 3
    print(x+y+s)


def f2():
    x = 5
    y = 6
    print(x+y+s)


f1()
f2()

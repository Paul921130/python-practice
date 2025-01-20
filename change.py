a = 10


def change(num):
    # num = a (copy by value)
    num = 20
    print(num)
    return num


change(a)
print(a)

b = [1, 2, 3, 4, 5]


def change(list):
    # list = b (copy by reference)
    list[0] = 100
    print(list)
    return list


change(b)
print(b)

c = 10
# can we change the value of c using change() function?


def change(num):
    global c
    c = 25


change(c)
print(c)

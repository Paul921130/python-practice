#
def sum(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum(1, 2, 3, 4, 5, 6, 7, 8))  # 36

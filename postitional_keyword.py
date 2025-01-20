#
def exponent(a, b):
    return a ** b


# postional arguments
print(exponent(2, 3))  # 8
print(exponent(3, 2))  # 9

# keyword arguments
print(exponent(a=2, b=3))  # 8
print(exponent(b=3, a=2))  # 8

mylist = [1, 2, 3, 4, 5, 6, 7, 8]
print(sorted(mylist, reverse=True))  # [8, 7, 6, 5, 4, 3, 2, 1]
# mylist is a positional argument
# reverse=True is a keyword argument

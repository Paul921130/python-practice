x = [1, 2, 3, 4, 5]
x_squared_generator = (i**2 for i in x)
print(x_squared_generator)

for i in x_squared_generator:
    print(i)

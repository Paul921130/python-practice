# Lambda variable:operation

a = (lambda x: x**2)(5)
print(a)

b = (lambda x, y: (x + y, x*y))(2, 3)
print(b)

for item in map(lambda x: x**2, [10, 22, 32, 112]):
    print(item, end=' ')


for item in filter(lambda x: x % 2 == 0, [1, 2, 3, 4]):
    print(item, end=' ')

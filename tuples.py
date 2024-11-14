mytuples = (10, 100, "Hello", "World")
print(len(mytuples))  # 4
print(mytuples[0:2])  # (10, 100)
print(mytuples.count(10))   # 1
print(mytuples.index("Hello"))  # 2

x = 10, 15, 17, 100  # tuple packing
print(x)  # (10, 15, 17, 100)
print(type(x))  # <class 'tuple'>


y = ("Wilson", 25)

name, age = y
print(y[0])  # Wilson
print(y[1])  # 25
print(name)  # Wilson
print(age)  # 25 variable names have meanings

a, b = (15, 199)
print(a)  # 15
print(b)  # 199

s = 25
d = 35
s, d = d, s
# tuple packing
# tuple unpacking

print(s)
print(d)


f = ([1, 2, 3], "Wilson")
f[0][1] = 200
print(f)  # ([1, 200, 3], 'Wilson')
# 如果tuple裡面的元素為可變的，則可以修改。如上面的list
# 但如果想要把tuple作為dict的key的話，那所有的元素必須使用immutable的

# 以下哪些可以作為dict的key
# 15 yes
# “Bob” yes
# ("Tom", [14,23,27]) nope
# ["filename",(15,16)] nope
# "filename" yes
# ("filename", 25, "extension") yes

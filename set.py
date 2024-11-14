myset = set({1, 2, 3})
print(myset)  # set()


mylist = [1, 2, 3, 1, 4, 2, 5, 5]
myset = set(mylist)
print(myset)  # {1, 2, 3, 4, 5}

s = set()
s.add(1)
print(s)  # {1}
s.add(2)
print(s)  # {1, 2}
s.discard(1)
print(s)  # {2}
s.clear()
print(s)  # set()


a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
print(a.difference(b))  # {1, 2} a - b
print(b.difference(a))  # {8, 6, 7} b - a
# 交集
print(a.intersection(b))  # {3, 4, 5} a & b
print(b.intersection(a))  # {3, 4, 5}  b & a
# 聯集
print(a.union(b))
print(b.union(a))

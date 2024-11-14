x = [4, 3, 2, 1]
y = sorted(x)
z = sorted(x, reverse=True)  # keyword argument
print(x)  # [4, 3, 2, 1]
print(y)  # [1, 2, 3, 4]
print(z)  # [4, 3, 2, 1]

# tuple
x = (4, 2, 3, 1)
y = sorted(x)
print(x)  # (4, 2, 3, 1)
print(y)  # [1, 2, 3, 4]

# dict keys
x = {"name": "Paul", "age": 25, "city": "New York"}
y = sorted(x)
print(x)  # {'name': 'Paul', 'age': 25, 'city': 'New York'}
print(y)  # ['age', 'city', 'name']

# set unordered collection of unique elements
x = {4, 3, 2, 1, 5}
y = sorted(x)
print(x)  # {1, 2, 3, 4, 5}
print(y)  # [1, 2, 3, 4, 5]

# string
x = "How are you doing today?"
y = sorted(x)
print(x)  # How are you doing today?
print(y)  # [' ', ' ', ' ', ' ', ' ', 'H', 'a', 'a', 'd', 'd', 'e', 'g', 'i', 'n', 'o', 'o', 'o', 'r', 't', 'u', 'w', 'y', 'y']

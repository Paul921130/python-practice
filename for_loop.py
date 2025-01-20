# for variable in iterable:
#     code block
for letter in 'Python':
    if (letter == letter.upper()):
        print('Upper Case Letter:', letter)
    else:
        print('Current Letter:', letter)


# a list of tuples
for tuple in [(1, 2), (3, 4), (5, 6)]:
    print(tuple[0]+tuple[1])  # tuple
for (a, b) in [(1, 2), (3, 4), (5, 6)]:
    print(a+b)  # tuple unpacking

# dictionary(keys)
mydict = {'name': 'John', 'age': 25, 'job': 'Developer'}
for key in mydict:
    print(key, mydict[key])

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(f"{key} is {value}")

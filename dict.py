person = {
    "name": "paul",
    "age": 32
}
print(person["name"])  # paul
print(person["age"])  # 32


x = {"name": "Wilson"}
print(x)
x["name"] = "Grace"
x["age"] = 22
print(x)

print(x.keys())  # Loop
print(x.values())
print(x.items())  # something like a list of tuples
# dict_keys(['name', 'age'])
# dict_values(['Grace', 22])
# dict_items([('name', 'Grace'), ('age', 22)])

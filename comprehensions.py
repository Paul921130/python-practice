x = [1, 2, 3, 4, 5]
squared_x = []  # List, dict, set
for i in x:
    squared_x.append(i**2)  # 我猜append就像push一樣


y = [1, 2, 3, 4, 5, 6]
squared_y = [i**2 for i in y]  # List comprehension
print(squared_x)
print(squared_y)


x_squared_dict = {i: i**2 for i in x if i > 2}  # Dict comprehension
print(x_squared_dict)

x_squared_set = {item**2 for item in x}  # Set comprehension
print(x_squared_set)

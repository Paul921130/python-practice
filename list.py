friend1 = "Mike"
friend2 = "Tom"
friend3 = "Jenny"
friend4 = "Sunny"
print(f"{friend1},{friend2},{friend3},{friend4}")
friend_list = ["Mike", "Tom", "Jenny", "Sunny"]
print(f"{friend_list[3]},{friend_list[2]},{friend_list[1]},{friend_list[0]}")
print(len(friend_list))
friend_list.insert(1, "Paul")
print(friend_list)


lucky_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(lucky_numbers[0:3])  # [1, 2, 3]
print(lucky_numbers[3:])  # [4, 5, 6, 7, 8]
print(lucky_numbers[::-1])  # [8, 7, 6, 5, 4, 3, 2, 1]


x = [1, 2, 3]
y = [4, 5, 6]
print(x+y)  # [1, 2, 3, 4, 5, 6]


friend_list = ["Mike", "Tom", "Jenny", "Sunny"]
friend_list.reverse()
print(friend_list)  # ['Sunny', 'Jenny', 'Tom', 'Mike']
friend_list = friend_list[::-1]
print(friend_list)

friend_list.append("Paul")
print(friend_list)

friend_list = ["Mike", "Tom", "Jenny", "Sunny"]
my_lost_friend = friend_list.pop()
print(friend_list)  # ['Mike', 'Tom', 'Jenny']
print(my_lost_friend)  # Sunny

# copy by reference
x = [1, 2, 3, 4, 5]
y = x
y[0] = 15
print(x)  # [15, 2, 3, 4, 5]
print(y)  # [15, 2, 3, 4, 5]

y = x.copy()
y[0] = 20
print(x)  # [15, 2, 3, 4, 5]
print(y)  # [20, 2, 3, 4, 5]

print("----------------")
# copy by value
a = 10
b = a
b = 15
print(a)  # a = 10? 15?
print(b)  # b = 15

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x[len(x)-1])
print(x[-1])

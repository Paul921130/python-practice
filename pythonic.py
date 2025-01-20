a = 10
b = 5
c = 20

# a = 20, b = 10, c = 5
# temp = a
# a = b
# b = temp

a, b = b, a  # pythonic way
a, b, c = c, a, b  # pythonic way

print(a, b)

# get_user_id(id)


def ger_user_id(id):
    return 'John', 22


name, age = ger_user_id(id)  # pythonic way
print(name, age)

bb = 50
if 10 < bb < 100:
    print('bb is in range')

cmd = input("Give a command: ")
# menbership operator
if cmd in ['dir', 'cd', 'echo']:
    print("Valid command")
else:
    print("Invalid command")

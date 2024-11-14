x = "Wilson"
print(type(x))

y = 3
print(type(y))


def hello():
    print("hello")


print(hello)  # <function hello at 0x104a96340>
print(hello())
# hello
# None

print(0.1 + 0.2 - 0.3)  # 5.551115123125783e-17

my_num_list = [1, 2, 3, 4, 5, 6, 6]
my_string = "|".join(str(i) for i in my_num_list)
print(my_string)  # 1|2|3|4|5|6|6

my_string_list = ["1", "2", "3", "4", "5", "6", "6"]
my_string = "|".join(my_string_list)
print(my_string)  # 1|2|3|4|5|6|6

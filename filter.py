#
def even(num):
    return num % 2 == 0


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in filter(even, my_list):
    print(item)

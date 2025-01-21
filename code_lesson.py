import random

secret_number = random.randint(1, 100)
min_number = 1
max_number = 100
# print(secret_number)

while True:
    input_number = input(f"終極密碼～～ {
                         min_number}-{max_number}   ")

    if int(input_number) < secret_number:
        print("再大一點")
        min_number = input_number
        continue
    if int(input_number) > secret_number:
        print("再小一點")
        max_number = input_number
        continue
    if secret_number == int(input_number):
        print("你答對了")
        break

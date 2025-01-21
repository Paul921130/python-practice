
import random

row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]

while True:
    if result := any([row1[0] == row1[1] == row1[2] == "O",
                      row2[0] == row2[1] == row2[2] == "O",
                      row3[0] == row3[1] == row3[2] == "O",
                      row1[0] == row2[0] == row3[0] == "O",
                      row1[1] == row2[1] == row3[1] == "O",
                      row1[2] == row2[2] == row3[2] == "O",
                      row1[0] == row2[1] == row3[2] == "O",
                      row1[2] == row2[1] == row3[0] == "O"]):
        print("O win!")
        break

    if result := any([row1[0] == row1[1] == row1[2] == "X",
                      row2[0] == row2[1] == row2[2] == "X",
                      row3[0] == row3[1] == row3[2] == "X",
                      row1[0] == row2[0] == row3[0] == "X",
                      row1[1] == row2[1] == row3[1] == "X",
                      row1[2] == row2[2] == row3[2] == "X",
                      row1[0] == row2[1] == row3[2] == "X",
                      row1[2] == row2[1] == row3[0] == "X"]):
        print("X win!")
        break

    def print_board(r1, r2, r3):
        print(r1)
        print(r2)
        print(r3)

    def user_input():
        row = int(input("請輸入列數(1-3)："))
        col = int(input("請輸入行數(1-3)："))
        while row not in [1, 2, 3] or col not in [1, 2, 3]:
            row = int(input("請輸入列數(1-3)："))
            col = int(input("請輸入行數(1-3)："))
        return row, col

    input_row, input_col = user_input()
    print(input_row, input_col)

    if input_row == 1:
        row1[input_col-1] = "O"

    if input_row == 2:
        row2[input_col-1] = "O"

    if input_row == 3:
        row3[input_col-1] = "O"

    computer_row = 1
    computer_col = 1

    def computer_input():
        computer_row = random.randint(1, 3)
        computer_col = random.randint(1, 3)
        return computer_row, computer_col

    computer_row, computer_col = computer_input()

    if computer_row == 1:
        row1[computer_col-1] = "X"

    if computer_row == 2:
        row2[computer_col-1] = "X"

    if computer_row == 3:
        row3[computer_col-1] = "X"

    print_board(row1, row2, row3)

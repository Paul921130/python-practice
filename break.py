# 使用break關鍵字來終止迴圈
print("在for迴圈中使用break")
for i in "123456789":
    if i == "5":
        break
    else:
        print(i)

print("執行完迴圈後的程式")


for i in "123456789":
    for j in "abcde":
        if j == "c":
            break
        print(i, j)

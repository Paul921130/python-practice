if True:
    print("This is true")
else:
    print("This is false")


age = 15

if age < 8:
    print("你好小")
elif age < 18:
    print("你有點大")
else:
    print("你好大")

# 8歲以下免費
# 8到65歲300元
# 65以上半價
if age < 8:
    print("免費")
elif 8 <= age < 65:
    print("300元")
elif 65 <= age < 110:
    print("半價")
else:
    print("你是外星人")

if (5 > 3) and []:
    print("True")
else:
    print("False")

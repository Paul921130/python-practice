# %%
# 詢問user的名字
# 有多少現金
# 餓不餓
# 檢查user有沒有30塊，如果有，就要吃早餐
#
name = input("What is your name? ")
print("你的名字是: ", name)
# 一定要整數不然報錯
cash = int(input("How much cash do you have? "))

hungry = input("Are you hungry? Y/N")

if cash >= 30 and hungry == "Y":
    print(name+" "+"Eat breakfast")

if cash < 30:
    print("你好窮喔")

if hungry == "Y":
    if cash >= 30:
        print("您該吃早餐了")
    elif cash < 30:
        print("您的錢不夠吃早餐")
elif hungry == "N":
    print("您不餓")
    if cash >= 30:
        print("您有錢可以買早餐")
    else:
        print("您不餓也沒錢")
else:
    print("請輸入Y/N")
# %%

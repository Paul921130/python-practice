# Struchtural Pattern Matching
# Python 3.10
# switch statement
name = input("你名字是: ")


def hello(name):
    match name:
        case "Alice":
            print("Hello, Alice!")
        case "Bob":
            print("Hello, Bob!")
        case _:
            print("Hello, stranger!")

 # match name:
#       case "Alice":
#           print("Hello, Alice!")
#       case "Bob":
#           print("Hello, Bob!")
#       case _:  # default
hello(name)

day = input("今天星期幾: ")
match day:
    case "星期六" | "星期天":
        print("耶！今天休假")
    case _:
        print("今天要上班")

command = input("你要去哪裡")
match command.split(" "):
    case ["go", "home"]:
        print("回家")
    case ["go", "school"]:
        print("去學校")
    case _:
        print("不知道你要去哪裡")

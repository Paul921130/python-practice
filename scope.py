name = "Wilson"


def greet():
    name = "Eric"
    hi()

    def hello():
        print(f"Hello, {name}")
    hello()


def hi():
    print(f"Hi, {name}")


hi()
greet()

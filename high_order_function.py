def high_order_function(func):
    func()


def small_func():
    print("I am a small function")


high_order_function(small_func())

string = "Aloha"
print(len(string))  # 5
print(int("200"))  # 200
print(float("200.5"))  # 200.5
print(str(200))  # 200

name = "Wilson"
# object-oriented programming (OOP)
print(name.upper())  # WILSON
# Python most of the methods dose not change the original string


name = "Wilson"
# object-oriented programming
print(name.upper())  # "WILSON"
# Python most of the methods dose not change the original string
name = name.upper()
# 這樣就能把name改成"WILSON"
print(name.upper().isupper())  # True

name2 = "Wilson"
print(name2.lower())  # wilson
print(name2.lower().islower())  # True
print(name2.index("s"))  # 3


name = "Josh Donaldson"
print(name.replace("Josh", "Paul"))  # Paul Donaldson
name2 = "Josh Jordan"
print(name2.replace("J", "I"))

sentence = "Today is a good day."
print(sentence.split(" "))  # ['Today', 'is', 'a', 'good', 'day.']
# ['T', 'o', 'd', 'a', 'y', ' ', 'i', 's', ' ', 'a', ' ', 'g', 'o', 'o', 'd', ' ', 'd', 'a', 'y', '.']
print(list(sentence))

# string, boolean, number, list, tuple, dictionary, set
# format(), f-string
sentence = "Today is a good {}.".format("boy")
print(sentence)  # Today is a good day.
sentence = "Today is {}.".format(20)
print(sentence)  # Today is 20.
sentence = "Today is {}.".format(["a", "Hello", "22", 32])
print(sentence)  # Today is ['a', 'Hello', '22', 32].
sentence = "{},{},{}".format("a", "b", "c")
print(sentence)  # a,b,c
sentence = "{2},{1},{0}".format("a", "b", "c")  # 花括號裡面放index
print(sentence)  # c,b,a
sentence = "{2},{1},{0}".format(*["a", "b", "c"])  # *是把list裡面的元素拆開
print(sentence)  # c,b,a
sentence = "{name},{age},{address}".format(
    name="Paul", age=22, address="Taipei")
print(sentence)  # Paul,22,Taipei
sentence = "{name},{age},{address}".format(
    **{"name": "Paul", "age": 22, "address": "Taipei"})
print(sentence)  # Paul,22,Taipei

myName = "paul"
age = 32
print(f"Hello, my name is {myName} and I am {age} years old.")
# Hello, my name is paul and I am 32 years old.
print(f"Hello, my name is {myName.upper()} and I am {age} years old.")
# Hello, my name is PAUL and I am 32 years old.

string = 'Good day is a good day.'
print(string.count("Good"))  # 1
print(string.lower().count("good"))  # 2
print(string.find("day"))  # 5

print(string.startswith("Good"))  # True
print(string.endswith("day."))  # True
print(string.endswith("day"))  # False

name = "Sam"
name = "P"+name[1:]
print(name)
print((name + " ") * 10)

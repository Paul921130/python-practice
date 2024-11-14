str = "abcd"
if "a" in str:
    print("a is in str")
else:
    print("a is not in str")

mystring = "Hello World"
isIn = False
for i in range(len(mystring)):
    if mystring[i] == "W":
        isIn = True
        break
print(isIn)

myString = "hello"
# slicing
# string[start(inclesive):stop(exclusive):step(optinal)]
# exclusive:排除的意思，是不包含stop的
# step:從start到stop是走幾步（以2為例則每步走2）
print(myString[0:3])  # hel
print(myString[:3])  # hel
print(myString[2:])  # llo
print(myString[::-1])  # olleh
print(myString[::2])  # hlo
print("I said good 'morning.'")
print("I said good \n 'morning.'")

mystring1 = "Hello"
mystring2 = "World"
result = mystring1+" "+mystring2
print(result)  # HelloWorld

teststring1 = "test"
teststring2 = 1
# TypeError: can only concatenate str (not "int") to str
# print(teststring1+teststring2)
# 透過str()轉換成字串
print(teststring1+str(teststring2))

string = "Hello"
string[0] = "h"
# print(string)

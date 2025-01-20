# default argument
def sum(a1=0, a2=0):
    return a1+a2


print(sum(1, 2))
print(sum(1))
# keyword argument
sum(a2=2, a1=1)

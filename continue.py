#
for i in "ABCDEF":
    if i == "D":
        continue
    print(i)
print("After continue")

for a in "1234567":
    print(a)
    continue
    print("This is after continue")

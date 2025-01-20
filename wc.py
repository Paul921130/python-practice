from sys import argv
# this is how we get
# the argv feature from the sys module
print(argv)

if len(argv) < 2:
    print("Usage: python wc.py filename")
    exit(1)
else:
    filename = open(argv[1])
    lines = filename.read()
    lines = lines.split("\n")
    line_count = len(lines)
    word_count = 0
    letter_count = 0
    for line in lines:
        words = line.split(" ")
        word_count += len(words)
        letter_count += len(line)

    print(type(lines))
    print(lines)
    print("幾行", line_count)
    print("多少字元", word_count)
    print("多少字母", letter_count)

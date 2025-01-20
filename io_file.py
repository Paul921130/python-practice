
file = open("myfile.txt")
print(file)
print(file.read())
print("-----------------")
open('myfile.txt', 'w').write('幹你娘2\n幹你娘3\n幹你娘4\n')

# 1. file = open(filename) - opens a file and returns it as a file object.
# 2. [file.read](http://file.read)() - returns the specified number of bytes from the file.
# 3. file.readline() - returns a line of text of our current position.
# 4. file.readlines() - returns a list containing each line in the file as a list item.
# 5. file.seek(offset) - sets the files current postition at the offset.
# 6. file.close()
file = open("myfile.txt")
print(file.readlines())
# file = open("myfile.txt")

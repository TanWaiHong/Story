with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="w") as file:
    file.write("New text.")

with open("my_file.txt") as file:
    contents = file.readlines()
    print(contents)

file = open("my_file.txt")
print(file.read())
file.close()

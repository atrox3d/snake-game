#
#   normal
#
my_file = open("my_file.txt")
text = my_file.read()
print(text)
my_file.close()
#
#   using with
#
with open("my_file.txt") as my_file:
    text = my_file.read()
    print(text)

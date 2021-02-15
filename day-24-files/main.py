#
#   read from file normal
#
my_file = open("my_file.txt")
text = my_file.read()
print(text)
my_file.close()
#
#   read from file using with
#
with open("my_file.txt") as my_file:
    text = my_file.read()
    print(text)
    # file gets closed automatically
#
#   write to file, overwrite
#
# with open("my_file.txt") as file:
#     file.write("overwrite contents")    # io.UnsupportedOperation: not writable
with open("my_file.txt", mode="w") as file:
    file.write("overwrite contents")
#
#   write to file, append
#
with open("my_file.txt", mode="a") as file:
    file.write("append contents")

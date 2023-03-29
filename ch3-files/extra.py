my_file = open("newfile.txt", "r")

# list_contents = my_file.read()
# print("read:", list_contents)

array_contents = my_file.readlines()
print ("readlines: ", array_contents)

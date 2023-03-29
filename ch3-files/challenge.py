import os
from os import path

# path to current directory
cwd = os.getcwd()
path = [cwd, "results", "results.txt"]

# create directory
if not os.path.exists(os.path.join(cwd, "results")):
    os.mkdir("results")

# Create a path and name for the file being created below.
file_path = os.path.join(*path)
# print(file_path)

# create file indicating its name and the directory in which it should be created using 'file_path'
result = open(file_path, "w+")

#  create list of files in current directory. You need to add a path to specify a different directory
files = os.listdir()

#calulate the size of files in bytes
total_bytes = sum(os.path.getsize(file) for file in files if os.path.isfile(file))
# print("bytecount:", total_bytes)

result.write(f"Total bytecount: {total_bytes} \n\nFiles list: \n\n-------------- \n\n" )

for file in files:
    # only add files
    if os.path.isfile(file):
        # print(file)
        result.write(f"{file} \n")
result.close()
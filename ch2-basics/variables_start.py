# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
my_int = 5
my_float = 13.2
my_str = "This is a string"
my_bool = True
my_list = [0, 1, "two", 3.2, False]
my_tuple = (0, 1, 2)
my_dict = {"one" : 1, "two" : 2}

print(my_int)
print(my_float)
print(my_str)
print(my_bool)
print(my_list)
print(my_tuple)
print(my_dict)

# re-declaring a variable works

my_int = "abc"
print(my_int)

# to access a member of a sequence type, use []

print(my_list[0], my_tuple[2])

# use slices to get parts of a sequence

print(my_list[1:5]) 
print(my_list[1:5:2]) # skip every second item 2 is the step value.

# you can use slices to reverse a sequence
print(my_list[::-1])

# dictionaries are accessed via keys
print(my_dict["one"])

# ERROR: variables of different types cannot be combined
print(str(5) + "hello world")

# Global vs. local variables in functions
def someFunction():
    my_int2 = 24 # local variable
    print(my_int2)

someFunction() # 24
#undefined
# print(my_int2)

def someOtherFunction():
    global my_str # declare as global variable
    my_str = "def" # change value of global variable
    print(my_str)

someOtherFunction()
print(my_str) 


del my_str # delete a variable
print(my_str) #undefined


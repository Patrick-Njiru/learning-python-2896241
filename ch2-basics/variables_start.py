# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works

myint = "abc"
print(myint)

# to access a member of a sequence type, use []

print(mylist[0], mytuple[2])

# use slices to get parts of a sequence

print(mylist[1:5]) 
print(mylist[1:5:2]) # skip every second item 2 is the step value.

# you can use slices to reverse a sequence
print(mylist[::-1])

# dictionaries are accessed via keys
print(mydict["one"])

# ERROR: variables of different types cannot be combined
print(str(5) + "hello world")

# Global vs. local variables in functions
def someFunction():
    myint2 = 24 # local variable
    print(myint2)

someFunction() # 24
#undefined
# print(myint2)

def someOtherFunction():
    global mystr # declare as global variable
    mystr = "def" # change value of global variable
    print(mystr)

someOtherFunction()
print(mystr) 


del mystr # delete a variable
print(mystr) #undefined


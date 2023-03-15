# create a palindrome checker that includes alphanumeric but not special characters or spaces.
import re

def palindromechecker():
    # strlist = list(str) # create a list from a string.
    name = input("Hello! What is your name? ")
    print("Nice to meet you, " + name + ". Let's get started." )
    rerun = True
    while (rerun):
        str = input("Add a word or sentence to check if it is a palindrome or 'exit' to stop : ")
        strlist = re.findall("[a-zA-Z-0-9]",str.lower()) # pick only numbers and letters from the string and create a list
        if str == 'exit':
            return "See you next time "+ name + "."
        elif strlist == strlist[::-1]:
            print(True)
        else:
            print(False)

palindromechecker()
import re

"""Compiles a regular expression pattern into a regular expression object, 
which can be used for matches using match(), search()"""
pattern_letter = re.compile("[A-Z]")

def evaluate(input):
     
    if pattern_letter.match(input):
        print("\n The string starts with an uppercase letter")
    else:
        print("\n The string does not start with an uppercase letter")


if __name__ == "__main__":
    
    input = input("Enter a string: ")
    evaluate(input)
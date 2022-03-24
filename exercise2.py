import re


def evaluate(input):
     
    if re.search("\d", input): # "/d" Matches any decimal digit; this is equivalent to the class [0-9]
        print("\n The string contains at least one number")
    else:
        print("\n The string doesn't contain any number")


if __name__ == "__main__":
    
    input = input("Enter a string: ")
    evaluate(input)
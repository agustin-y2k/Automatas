import re


def evaluate_number(input_number):
    if re.search("7", input_number):
        print("\n The string contains at least one number 7")
    else:
        print("\n The string does not contain a number 7")


def evaluate_letter(input_letter):
    if re.search("(p|P)", input_letter):
        print("\n The string contains at least one letter p")
    else:
        print("\n The string does not contains a letter p")


def evaluate_first_element(input):
    
    pattern_number = re.compile("[0-9]")
    pattern_letter = re.compile("[a-zA-Z]")
    
    if pattern_number.match(input):
        evaluate_number(input)
    elif pattern_letter.match(input):
        evaluate_letter(input)
    else:
        print("\n The string does not start with a letter or number")


if __name__ == "__main__":
    
    input = input("Enter a string: ")
    evaluate_first_element(input)
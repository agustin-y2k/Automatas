from nis import match
import re

def evaluate(input):
    # https://regex101.com
    triple_quote = re.compile("\"{3}(.|[\r\n])*\"{3}")
    single_quote = re.compile("\'{3}(.|[\r\n])*\'{3}")
    
     
    if re.match("#",input):
        print("\n This is a simpleline comment")
    elif re.fullmatch(triple_quote, input):
        print("\n This is a multiline comment using triple quote")
    elif re.fullmatch(single_quote, input):
        print("\n This is a multiline comment using single quote")
    else:
        print("\n Is not a comment")


if __name__ == "__main__":
    
    input = input("Enter a string: ")
    evaluate(input)

import re

# [a-zA-z0-9._-]+@[\w]+\.[net|com|biz]{3,}(\.[nl|us|uy|ca|ar]{2,})?$

regex = re.compile("[a-zA-z0-9._-]+@[\w]+\.[net|com|biz]{3,}(\.[nl|us|uy|ca|ar]{2,})?$")
pattern_letter = re.compile("[a-zA-Z]")

def validate(email):

    if pattern_letter.match(email):
      if regex.match(email):
        print("{} Valid email!".format(email))
      else:
        print("{} Invalid email!".format(email))
    else:
      print("{} Invalid email!".format(email))

if __name__ == "__main__":
  
    print("\n")
    f = open("email.txt","r")
    for string in f:
        validate(string)  
        print("\n-----------------------------------------------------\n")
    f.close()

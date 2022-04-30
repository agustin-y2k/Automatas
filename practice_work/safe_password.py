import re

f = open("password.txt","r")
string = f.readline()
for string in f:
    print("\n",string)
    size = len(string)
    if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$_.-])[A-Za-z\d@#$_.-]{8,}$', string):
        print('Password is strong')
    else:
        print('Invalid password, to weak')

f.close()
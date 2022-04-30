#Dirección IPv4 (000.000.000.000-255.255.255.255)
import re

regex = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")


f = open("ipv4.txt","r")
string = f.readline()
for string in f:
    print("\n",string)
    if regex.search(string):
        print("Valid address\n")
    else:
        print("Invalid address\n")

f.close()
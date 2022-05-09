#Dirección IPv4 (000.000.000.000-255.255.255.255)
import re
from pyparsing import Regex

Regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

with open("ipv4.txt") as archivo:
    for linea in archivo:
        if re.fullmatch(Regex,linea.strip()):
            print(f"url: {linea.strip()}\n \t Expresion Correcta \t")
        else:
            print(f"url: {linea.strip()}\n \t Expresion Incorrecta \t")
        print("-------------------------------------------")

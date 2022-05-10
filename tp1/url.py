import re

Regex = "((http|https|HTTP|HTTPS)?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,3})(\/)?"

with open("./url.txt") as archivo:
    for linea in archivo:
        if re.fullmatch(Regex,linea.strip()):
            print(f"url: {linea.strip()}\n \t Expresion Correcta \t")
        else:
            print(f"url: {linea.strip()}\n \t Expresion Incorrecta \t")
        print("-------------------------------------------")

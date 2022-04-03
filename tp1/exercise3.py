from nis import match
import re

def evaluate(input):
    # https://regex101.com/r/dAW2mI/2 para que pruebes la expresion regular, andar anda pero si ves la pagina el ultimo caracter no lo esta analizando
    triple_quote = re.compile("\"{3}(.|[\r\n])*\"{3}")
    single_quote = re.compile("\'{3}(.|[\r\n])*\'{3}")
    
     
    if re.match("#",input):
        print("\n This is a simpleline comment")
    elif re.fullmatch(triple_quote, input):
        print("\n This is a multiline comment using triple quote")
    elif re.fullmatch(single_quote, input):
        print("\n This is a multiline comment using single quote")
    # Estaria bueno utilizar un or en vez de tanto if pero el operador | no estaria funcionando luego de la compilacion del pattern
    else:
        print("\n no paso")


if __name__ == "__main__":
    
    input = input("Enter a string: ")
    evaluate(input)

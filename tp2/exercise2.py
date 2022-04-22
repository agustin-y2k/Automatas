"""
def estado_0(lista, cont):
    print("estado 0")
    if len(lista) == 0:
        estado_8()
    estado_1(lista, cont)

def estado_1(lista, cont):
    if cont == 0:
        print("estado 1")
        cont += 1
        estado_2(lista, cont)
    elif cont == 1:
        print("estado 1")
        cont += 1
        estado_5(lista, cont)
    elif cont >= 2:
        cont = 0
        estado_1(lista, cont)

def estado_2(lista, cont):
    print("estado 2")
    if lista[0] == 'aa':
        lista[0] = 'a'
        estado_3(lista, cont)
    else:
        print("***********Reinicio**********")
        estado_0(lista, cont)

def estado_3(lista, cont):
    print("estado 3")
    if lista[0] == 'a':
        lista.pop(0)
        estado_4(lista, cont)
    else:
        print("***********Reinicio**********")
        estado_0(lista, cont)

def estado_4(lista, cont):
    print("estado 4")
    estado_7(lista, cont)

def estado_5(lista, cont):
    print("estado 5")
    if lista[0] == 'b':
        lista.pop(0)
        estado_6(lista, cont)
    else:
        print("***********Reinicio**********")
        estado_0(lista, cont)
    

def estado_6(lista, cont):
    print("estado 6")
    estado_7(lista, cont)

def estado_7(lista, cont):
    print("estado 7")
    if len(lista) == 0:
        estado_8(lista)
    elif len(lista) > 0:
        print("***********Reinicio**********")
        estado_1(lista, cont)

def estado_8(lista):
    print("estado 8")
    cont2 = 0
    if len(lista) == 0:
        estado_16()
    elif len(lista) > 0:
        estado_9(lista, cont2)

def estado_9(lista, cont):
    if cont == 0:
        print("estado 9")
        cont += 1
        estado_13(lista, cont)
    elif cont == 1:
        print("estado 9")
        cont += 1
        estado_10(lista, cont)
    elif cont >= 2:
        cont = 0
        estado_8(lista, cont)

def estado_10(lista, cont):
    print("estado 10")
    if lista[0] == 'bb':
        lista[0] = 'b'
        estado_11(lista, cont)
    else:
        print("***********Reinicio**********")
        estado_8(lista, cont)

def estado_11(lista, cont):
    print("estado 11")
    if lista[0] == 'b':
        lista.pop(0)
        estado_12(lista, cont)
    else:
        print("***********Reinicio**********")
        estado_8(lista, cont)

def estado_12(lista, cont):
    print("estado 6")
    estado_15(lista, cont)

def estado_13(lista, cont):
    print("estado 13")
    if lista[0] == 'a':
        lista.pop(0)
        estado_14(lista, cont)
    else:
        print("***********Reinicio**********")
        estado_8(lista, cont)

def estado_14(lista, cont):
    print("estado 14")
    estado_15(lista, cont)

def estado_15(lista, cont):
    print("estado 15")
    if len(lista) == 0:
        estado_16()
    elif len(lista) > 0:
        print("***********Reinicio**********")
        estado_9(lista, cont)

def estado_16():
    print("estado 16")
    print("Estado de Aceptacion")
    print("**********Fin del Programa**********")


def validador(lista_alfabeto, lista_convertida, cont):
    con = 0
    for i in lista_convertida:
        if lista_alfabeto.__contains__(lista_convertida[con]) == False:
            print(f"'{lista_convertida[con]}' argumentos ingresados no pertenecen al alfabeto")
            main()
        con += 1
    print(lista_convertida)
    estado_0(lista_convertida, cont)
    """
from pandas import notnull


def main():
    #lista_alfabeto = ['a','b','bb','aa']
    lista_string = list(input("ingrese el string:"))
    
    
    nueva_lista = []
    aux1 = ''
    aux2 = ''
    lista_string.append('')
    for i in range(len(lista_string)):
        if aux2 == '':
            aux2 = lista_string[i]
        else:
            if aux2 == lista_string[i]:
                nueva_lista.append(f'{aux2}{lista_string[i]}')
                aux2 = ''
            else:
                if aux2 != lista_string[i]:
                    nueva_lista.append(f'{aux2}')
                    aux2 = lista_string[i]
    print(lista_string)
    print(nueva_lista)
    
    cont = 0
    #validador(lista_alfabeto, nueva_lista, cont)


if __name__ == "__main__":
    main()
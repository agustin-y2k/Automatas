
def estado_0(lista):
    print(f"estado 0")
    if len(lista) == 0:
        print(f"estado 8")
        estado_8(lista)
    else:
        if lista[0] == 'aa' or lista[0] == 'b':
            estado_1(lista)
        elif lista[0] == 'bb' or lista[0] == 'a':
            print(f"estado 8")
            estado_8(lista)
        
def estado_1(lista):
    if lista[0] == 'aa':
        print(f"estado 1")
        print(f"estado 2 -> {lista[0]}")
        print(f"estado 3 -> {lista[0]}")
        print(f"estado 4")
        lista.pop(0)
    elif lista[0] == 'b':
        print(f"estado 1")
        print(f"estado 5 -> {lista[0]}")
        print(f"estado 6")
        lista.pop(0)
    estado_7(lista)

def estado_7(lista):
    print("estado 7")
    if len(lista) == 0:
        print(f"estado 8")
        estado_8(lista)
    else:
        if lista[0] == 'aa' or lista[0] == 'b':
            estado_1(lista)
        elif lista[0] == 'bb' or lista[0] == 'a':
            print("estado 8")
            estado_8(lista)

def estado_8(lista):
    if len(lista) == 0:
        estado_16()
    else:
        if lista[0] == 'bb':
            print(f"estado 9")
            print(f"estado 10 -> {lista[0]}")
            print(f"estado 11 -> {lista[0]}")
            print(f"estado 12")
            lista.pop(0)
        elif lista[0] == 'a':
            print(f"estado 9")
            print(f"estado 13 -> {lista[0]}")
            print(f"estado 14")
            lista.pop(0)    
        estado_15(lista)

def estado_15(lista):
    print("estado 15")
    if len(lista) == 0:
        estado_16()
    else:
        if lista[0] == 'aa' or lista[0] == 'b':
            print(f'**********Reinicio**********')
            estado_0(lista)
        elif lista[0] == 'bb' or lista[0] == 'a':
            estado_8(lista)
        
def estado_16():
    print("estado 16")
    print("Estado de Aceptacion")
    print("**********Fin del Programa**********")

def convertidor(lista_string):
    nueva_lista = []
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
    return nueva_lista  

import re

def main():
    con = 0
    estado = False
    while estado == False:
        string = input("ingrese el string:")
        if string=='':
            print("Debe ingresar un string")
        else:
            if re.fullmatch('[a-b]*', string):
                estado = True
                lista_string = list(string)
            else:
                print(f"ingrese un string valido")
                
    lista = convertidor(lista_string)
    print(f'lista: {lista}')
    estado_0(lista)
        
if __name__ == "__main__":
    main()
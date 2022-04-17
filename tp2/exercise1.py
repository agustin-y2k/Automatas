
def estado_0(lista, cont):
    print(f"estado 0")
    if len(lista) == 0:
        estado_7()
    estado_1(lista, cont)

def estado_1(lista, cont):
    if cont == 0:
        print("estado 1")
        cont += 1
        estado_2(lista, cont)
    elif cont == 1:
        print("estado 1")
        cont += 1
        estado_4(lista, cont)
    elif cont >= 2:
        cont = 0
        estado_1(lista, cont)

    
def estado_2(lista, cont):
    print("estado 2")
    if lista[0] == 'a':
        lista.pop(0)
        estado_3(lista, cont)
    else:
        print("***********Reinicio**********")
        estado_0(lista, cont)

def estado_3(lista, cont):
    print("estado 3")
    estado_6(lista, cont)

def estado_4(lista, cont):
    print("estado 4")
    if lista[0] == 'b':
        lista.pop(0)
        estado_5(lista, cont)
    else:
        print("***********Reinicio**********")
        estado_0(lista, cont)

def estado_5(lista, cont):
    print("estado 5")
    estado_6(lista, cont)

def estado_6(lista, cont):
    print("estado 6")
    if len(lista) == 0:
        estado_7()
    elif len(lista) > 0:
        print("***********Reinicio**********")
        estado_1(lista, cont)

def estado_7():
    print("estado 7")
    print("Estado de Aceptacion")
    print("**********Fin del Programa**********")


def main():
    #lista_alfabeto = list(input("ingrese el alfabeto: "))
    lista_string = list(input("ingrese el string:"))
    cont = 0
    estado_0(lista_string, cont)

#estado = True

main()
    
def stateA(n):

    if len(n) == 0:
        print("string not accepted")
    else:
        print("State A, input:", n[0])
        if n[0] == 'a':
            stateB(n[1:])
        elif n[0] == 'b':
            stateC(n[1:])


def stateB(n):

    if len(n) == 0:
        print("string not accepted")
    else:
        print("State B, input:", n[0])
        if n[0] == 'a':
            stateB(n[1:])
        elif n[0] == 'b':
            stateD(n[1:])


def stateC(n):

    if len(n) == 0:
        print("string not accepted")
    else:
        print("State C, input:", n[0])
        if n[0] == 'a':
            stateB(n[1:])
        elif n[0] == 'b':
            stateC(n[1:])


def stateD(n):

    if len(n) == 0:
        print("string not accepted")
    else:
        print("State D, input:", n[0])
        if n[0] == 'a':
            stateB(n[1:])
        elif n[0] == 'b':
            stateE(n[1:])


def stateE(n):

    if len(n) == 0:
        print("string accepted")
    else:
        print("State E, input:", n[0])
        if n[0] == 'a':
            stateB(n[1:])
        elif n[0] == 'b':
            stateC(n[1:])


print("Enter a string: ")
n = input()
stateA(n)

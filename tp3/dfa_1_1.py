def stateA(n):
    # if length of n become 0
    # then print accepted
    if len(n) == 0:
        print("string accepted")

    else:
        print("State A, input:", n[0])
        # 'a' found call stateB function
        # 'b' found call stateC function
        if n[0] == 'a':
            stateB(n[1:])
        elif n[0] == 'b':
            stateC(n[1:])


def stateB(n):
    # if length of n become 0
    # then print accepted
    if len(n) == 0:
        print("string accepted")

    else:
        print("State B, input:", n[0])
        # 'a' found call stateB function
        # 'b' found call stateC function
        if n[0] == 'a':
            stateB(n[1:])
        elif n[0] == 'b':
            stateC(n[1:])


def stateC(n):
    # if length of n become 0
    # then print not accepted
    if len(n) == 0:
        print("string accepted")

    else:
        print("State C, input:", n[0])
        # 'a' found call stateB function
        # 'b' found call stateC function
        if n[0] == 'a':
            stateB(n[1:])
        elif n[0] == 'b':
            stateC(n[1:])


print("Enter a string: ")
n = input()
stateA(n)

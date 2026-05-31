import sys

def Minimum(L):
    min = L[0]
    minI = 0
    for i in range(1, len(L)):
        if L[i]<min:
            min = L[i]
            minI = i
    return minI

def Sort(L):
    L2 = []
    while L:
        L2.append(L.pop(Minimum(L)))
    return L2


L = eval(sys.argv[1])
print(Sort(L))

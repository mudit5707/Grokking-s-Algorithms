import sys

def QSort(L):
    if len(L) <2:
        return L
    LArray = []
    RArray = []
    Pivot = L[0]
    for i in L[1:]:
        if i<Pivot:
            LArray.append(i)
        else:
            RArray.append(i)
    return QSort(LArray) + [Pivot] + QSort(RArray)

L = eval(sys.argv[1])
print(QSort(L))
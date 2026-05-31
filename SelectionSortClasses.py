class JustSort():
    def __init__(self, value):
        self.value = value
    
    def Minimum(self):
        min = self.value[0]
        minI = 0
        for i in range(1, len(self.value)):
            if self.value[i]<min:
                min = self.value[i]
                minI = i
        return minI
    
    def Sort(self):
        L = self.value
        L2 = []
        while L:
            L2.append(L.pop(self.Minimum()))
        return L2
    
ListObject = JustSort([7,5,2,6,9,3])
print(ListObject.Sort())

#create a class c-2d vector and use it to create another class representing a 3d vector

class c2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"




class c3dVec(c2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v2d = c2dVec(1, 3)
v3d = c3dVec(1, 9, 7)
print(v2d)
print(v3d)
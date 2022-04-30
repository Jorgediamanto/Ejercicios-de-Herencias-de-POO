class punto2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def traslacion(self,a,b):
        self.x=self.x+a
        self.y=self.y+b
    def mostrar(self):
        return f'X: {self.x}; Y: {self.y}'

class punto3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def traslacion(self,a,b,c):
        self.x=self.x+a
        self.y=self.y+b
        self.z=self.z+c
    def mostrar(self):
        return f'X: {self.x}; Y: {self.y}; Z: {self.z}'

a = punto2D(1, 2)
print(f'A = {a.mostrar()}')

a.traslacion(-1, -2)
print(f'A = {a.mostrar()}')

b = punto2D(-3, 0) 
print(f'B = {b.mostrar()}') 

b.traslacion(5, -1) 
print(f'B = {b.mostrar()}') 


c = punto3D(1,5,-3)
c.traslacion(0, -2, 1)
print(f'C = {c.mostrar()}')

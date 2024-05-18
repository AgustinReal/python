class Shape:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    
    def draw(self):
        pass

class Circulo(Shape):
    def __init__(self, x, y, height, width, raidus):
        super().__init__(x, y, height, width)
        self.raidus = raidus
    def draw(self):
        print(f"Imprimiendo la forma de un circulo {self.x} x {self.y} y su radio es {self.raidus}")

class Triangulo(Shape):
    def __init__(self, x, y, height, width, base):
        super().__init__(x, y, height, width)
        self.base = base
    
    def draw(self):
        print(f"Imprimiendo un triangulo en {self.x} x {self.y} con una base {self.base} y una altura {self.height}")

class Rectangulo(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)

    def draw(self):
        print(f"Imprimiendo un rectangulo con sus medidas {self.x} x {self.y} y con su ancho de {self.width} y la altura de {self.height}")

circulo = Circulo(x=50, y=50, height=150, width=50, raidus=25)
triangulo = Triangulo(x=10, y=100, height=150, width=50, base=50)
rectangulo = Rectangulo(x=300, y=200, width=200, height=100)

circulo.draw()
triangulo.draw()
rectangulo.draw()
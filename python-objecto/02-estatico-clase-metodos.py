class MiClase:

    atributo_de_clase = 7

    def __init__(self, color):
        self.coor = color
    
    @staticmethod # define q es un metodo static
    def metodo_estatico():
        print("Este es un método estático...")

    @classmethod # define q es un metodo de clase
    def metodo_de_clase(cls): # Ideal para modificar los atributos de clase => cls. 
        print("Este es un método de clase con el atributo de clase", cls.atributo_de_clase)

miClase = MiClase("Yellow")

MiClase.metodo_estatico()

MiClase.metodo_de_clase()
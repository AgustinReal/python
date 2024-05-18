class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def Juega(self):
        print(f"La mascota {self.nombre} esta jugando")

class Perro(Mascota):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def Juega(self):
        super().Juega()
        print(f"El perro de raza {self.raza} juega con su hueso.")

class PerroDomestico(Perro):
    def __init__(self, nombre, raza, propietario):
        super().__init__(nombre, raza)# le mandamos los params a los padres
        self.propietario = propietario

    def Juega(self):
        super().Juega()
        print(f"El perro domestico mueve la cola")
    
    def Presentarse(self):
        print(f"hola, soy {self.nombre}, de raza {self.raza} y mi dueño es {self.propietario}")

perro_domestico = PerroDomestico("Max", "Pastor aleman", "Agus Real")

perro_domestico.Presentarse()

perro_domestico.Juega()
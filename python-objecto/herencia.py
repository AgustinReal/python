class Vehiculo:
    def __init__(self, marca, modelo, velocidad, anio):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.anio = anio

    # métodos
    def DarVelocidad(self, velocidad):
        self.velocidad += velocidad

    def ReducirVelocidad(self, velocidad):
        self.velocidad -= velocidad

#Asi se hereda de una clase padre => nombre del hijo (nombre del padre):
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad, anio, motor):
        super().__init__(marca, modelo, velocidad, anio)
        self.motor = motor
    
    # hacer wheelie
    def Wheelie(self):
        return "haciendo el wheelie...."
    
class Autobus(Vehiculo):
    def __init__(self, marca, modelo, velocidad, anio, asientos):
        super().__init__(marca, modelo, velocidad, anio,)
        self.asientos = asientos

    def CargarPasajeros(self, pasajeros):
        return f"pasajero a bordo {pasajeros}"

motocicleta = Motocicleta("Honda", 2022, 100, 2023, 1200)

# print(motocicleta.marca)
# print(motocicleta.Wheelie())

autobus = Autobus("Blubird", 2010, 100, 2000, 30)
print(autobus.marca)
print(autobus.CargarPasajeros(60))
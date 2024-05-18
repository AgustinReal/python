class Vehiculo:
    def __init__(self, marca, modelo ):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    # métodos
    def DarVelocidad(velocidad): # esto es una función
        # self.velocidad += velocidad
        print(velocidad)

    def ReducirVelocidad(self, velocidad): # metodo de clase
        self.velocidad -= velocidad
        print(self.velocidad)

vehiculo1 = Vehiculo("ford", 2020)

print(vehiculo1.marca)
print(vehiculo1.modelo)

vehiculo1.ReducirVelocidad(20)

Vehiculo.DarVelocidad(20)
Vehiculo.ReducirVelocidad(5)
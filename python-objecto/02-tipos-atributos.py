#atributos de clase: Son compartidos de forma general para todas las instancias de la clase.
#atributos de instancia: Son diferetes para cada una de las instancias que le asigna valores.
#atributos de datos: Son únicos pra la instancia en la que se crea y se inicializa.

class Vehiculo:

    #atributos de clase
    ruedas = 4

    #atributos de instancia
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    # métodos
    def DarVelocidad(self, velocidad):
        self.velocidad += velocidad

    def ReducirVelocidad(self, velocidad):
        self.velocidad -= velocidad

#atributos de instancia
vehiculo1 = Vehiculo("Ford", 2022, 20)
print("Instancia 1")
print(vehiculo1.ruedas)
print(vehiculo1.marca)
print(vehiculo1.modelo)
print(vehiculo1.velocidad)

print()
#atributo de clase
Vehiculo.ruedas = 6 # cambiar el valor de ruedas (atributos de clase) y esto cambia para todas las instancias
print()

vehiculo1.ruedas = 5 # cambio el valor de ruedas (solo a la instancia "vehiculo1")

vehiculo2 = Vehiculo("Mezda", 2020, 40)
print("Instancia 2")
print(vehiculo2.ruedas)
print(vehiculo1.ruedas)
# print(vehiculo1.marca)
# print(vehiculo1.modelo)
# print(vehiculo1.velocidad)

#atributos de datos
print("Vehiculo 2 - color")
vehiculo2.color = "black"

print(vehiculo2.color)
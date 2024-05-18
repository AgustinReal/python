import math

#constantes metematicas

print("pi: ", math.pi)
print("Numero de Euler", math.e) 

#Funciones trigonométricas

angulo = math.radians(45)
print(angulo)
print("Seno : ", math.sin(angulo))
print("Coseno : ", math.cos(angulo))
print("Tangente : ", math.tan(angulo))

#Funciones exponenciales
print("Exponenciales (e °2)", math.exp(2))

#Funciones logaritmicas
print("Log de 10 : ", math.log(10))

#Potencias
print("2 elevado al cubo : ", math.pow(2, 3))

#raices
print("Raiz cuadrado de 25: ", math.sqrt(25))

#Fracciones
from fractions import Fraction

fract1 = Fraction(3, 4)
fract2 = Fraction(1, 6)

suma = fract1 + fract2
resta = fract1 - fract2
multiplicacion = fract1 * fract2
division = fract1 / fract2

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", multiplicacion)
print("División: ", division)

from decimal import Decimal, getcontext

# Mayor precisión
getcontext().prec = 10

num1 = Decimal("0.1")
num2 = Decimal("0.2")

suma_decimal = num1 + num2

print("Suma decimal: ", suma_decimal)
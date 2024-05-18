# Tipos de datos

# NÚMERICOS
# Tipos
# int (Enteros) => 1, 1000, 100000, -300
# float (numeros con coma - decimales) => 2.1, -4.5, -500.5, 1000.33
# complex (complejos) => 2 + 1j, 1

# int

number1 = 300
number2 = -300




# float
number3 = 2.25


millon = 1e6


#=> la e(Cantidad de 0) indica la cantidad de 0, en este caso son 6 ceros.
print(millon)

# complex
number4 = 2 +1j

print(type(number1))
print(type(number2))
print(type(number3))
print(type(number4))

# STRINGS
# str (string) => "EDteam"

text = """este es un texto de ejemplo para 
saber como funciona la multilinea en los strings
de pyton""" # Con (""" text """ o ''' text ''') podemos describir cosas.
print(text)

# string
name = "Agustin"

print(name[0]) # acceder al indice especifico del string. En este caso al indice 0 => "A", en este caso al indice 1 => "g".


#BOOL
#bool (booleano) => true, false

name = "Agustin"

print(bool(name)) # De esta manera sabemos si tiene contenido la variable "name"
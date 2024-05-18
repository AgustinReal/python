"""
Ejecuta código de forma repetitiva mientras una condición se cumpla
y de como resultado True
"""
number = 1

while 10 > number and number > 0: # Condición: Esta porción de codigo se ejecutara hasta que no cunpla esta condición.
    print("Número : " + str(number))
    number += 1 # acumulador: Sumara 1 cada vez que number sea menor a 10.

print("\n" + str(number)) 
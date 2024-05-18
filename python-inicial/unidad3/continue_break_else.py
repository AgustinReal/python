"""
continue => permite saltar a la siguiente posición.
break => rompe (cancela) el ciclo.
else => ejecuta una porción de código cuando termina el ciclo.
"""

frameworks = ["Flask", "Django", "FastApi", "Pyramid"]

#continue
for f in frameworks:
    if f == 'Flask':
        print("Es Flask")
        continue # si es Flask salto a la sig recorrida del for
    print(f)

frameworks = ["Flask", "Django", "FastApi", "Pyramid"]

#break
for f in frameworks:
    if f == 'Flask':
        print("Es Flask")
        break # una vez que encuentre Flask, este cancela el bucle. 
    print(f)


frameworks = ["Flask", "Django", "FastApi", "Pyramid"]

#else
for f in frameworks:
    if f == 'Flask':
        print("Es Flask")
    print(f)
else: # se ejecuta cada vez que termine el for o el ciclo.
    print("El ciclo terminó")

#else / continue
number = 0

while number < 10:
    number += 1
    if number == 5:
        print("Es 5")
        continue # si es 5 salta a la sig recorrida del for
    print(number)
else: # se ejecuta cada vez que termine el for o el ciclo.
    print("El ciclo terminó")
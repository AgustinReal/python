"""
Genera código repetitivo similar a while
"""

# item =>Es valor de cada elemento que va recorrer el for.
# range => rango de valores a recorrer range(valor incial, valor final).
for item in range(1, 10): # => elegis el recorrido del 1 al 10 por ejemplo.
    print(item)

# range => rango de valores a recorrer range(valor incial, valor final, valor de escala).
# => elegis el recorrido del 2 al 10 por ejemplo y ademas si pones otro parametros ejemplo 3 va de 3 en tres.
for item in range(2, 10, 3): 
    print(item)

number = input("Ingrese un número: ")

for item in range(1, int(number) + 1 ): # => elegis el recorrido del 2 al 10 por ejemplo.
    print(item)

lenguajes = ["Python", "Go", "Javascript", "Rust"]

for lenguaje in lenguajes:
    print(lenguaje)

# for lenguaje in lenguajes:
#     if lenguaje == "Python":
#         print("El lenguaje de programcion es : " + lenguaje)

frameworks = ["Django", "Flask", "Piramid", "FastApi"]

for lenguaje in lenguajes:
    for framework in frameworks:
        print(framework, lenguaje)

saludo = "Buenas noches"

for letra in saludo: 
    print(letra)
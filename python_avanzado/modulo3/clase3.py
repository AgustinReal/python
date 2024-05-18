texto = """
Boca Juniors es uno de los clubes más emblemáticos y exitosos del fútbol argentino y mundial. 
Fundado el 3 de abril de 1905 en el barrio de La Boca, en la ciudad de Buenos Aires, 
este club ha dejado una marca indeleble en la historia del deporte rey.
"""
texto = texto.replace("Boca", "BOCA", 1) # De esta manera puedo sustituir un string por otra.
palabra_busqueda = input("ingrese palabra a buscar: ")
index = texto.find(palabra_busqueda) #Busca el indice con el parametro (palabra) ingresado y devulve la posición del indice de esa string.

if(index != -1):
    print(f"{palabra_busqueda} se encontro en el indice {index}")

    total_encontrados = texto.count(palabra_busqueda)
    print(f"{palabra_busqueda} aparece {total_encontrados} veces")
else:
    print("No se encontro la palabra a buscar")


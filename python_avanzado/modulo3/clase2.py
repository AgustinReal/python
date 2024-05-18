#concatenación
cadena1 = "Hola, "
cadena2 = 25

resultado = cadena1 + str(cadena2)

print(resultado.upper())#lo transformo a mayuscula la string

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Edad: "))
print("Hola mi nombre es " + nombre + " " + apellido)

#f-strings
saludo = f"hola mi nombres es {nombre} {apellido} y tengo {edad} años"
print(saludo)

#concatenar con listas
numeros =[1,2,3,4,5]
resultado = ""
for num in numeros:
    resultado += str(num) + " "

print(resultado)

#concatenar con join
palabras = ["Hola", "Mundo", "Python"]
frases = " " .join(palabras)
print(frases)
# List (listas - array), Info vuelve ordenada 

frutas = ["Manzana", "pera", "uva"] # => array de strings

numeros = [1, 2 ,3 ,4, 50] # => array de números

varios = [True, "Manzana", 20, 33.33, -300] # => array variado de datos.

print(type(frutas))

del frutas[1] # Elimino el elemnto pera.

print(numeros[4])# mostrar el 50

# print(frutas[-3])# mostrar Manzana


frutas2 = frutas[1:3] #[1 : 3] del indice del 1 al 3 
print(frutas2)

new_list = frutas + numeros

print(new_list)

print(len(frutas)) # lenght del array

new_list2 = [numeros, frutas]

print(new_list2)

print(new_list2[0][2]) #acceder aun elemento especifico

#Como eliminar un elemento de un Array, metodo "del".
del numeros[0] # [indice a eliminar] => De esta forma eliminamos un indice del array
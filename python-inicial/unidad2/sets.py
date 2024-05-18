#Es una tupla tmb
# Sets, la info no vuelve ordenada y ademas si tiene info repetida esta se remplazara y no la mostrara y no se le puede agragar elementos.

variado = {"Kevin", "John", "Doe", "Doe", True, 300, 1, 0, False}

mi_set_numeros = {8,1, 2, 3, 4, 5}


print(type(variado))# => obtner el tipo de dato
print(variado)
print(mi_set_numeros)

# otra forma se crear un set

frutas = set(("manzana", "pera", "uva"))

frutas.add(6)

frutas.discard(7) # No genera ningun error si el 7 no esta.
#frutas.remove(7) # Si genera un error si el 7 no esta.

print(frutas)

texto = "Este un ejemplo de texto para mostrar"

print(texto)

conjunto_vacio = set()


print(set(texto))

mi_set_con_duplicados = {1, 2, 2, 3, 3, 4, 5, 5}
print(mi_set_con_duplicados)  # Resultado: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2  # También puedes usar el método union()
union2 = set1.union(set2) # Metodo de union()

print(union)  
print(union2)

interseccion = set1 & set2  # También puedes usar el método intersection()
interseccion2 = set1.intersection(set2) # metodo de intersection()

print(interseccion) # => "Mediante &"  
print(interseccion) # => "Mediante intersection()"  
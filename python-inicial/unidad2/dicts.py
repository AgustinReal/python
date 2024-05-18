# Diccionarios, La info vuelve ordenada.

# crear uno dic
usuario = {
    "nombre" : "John",
    "apellido" : "Doe",
    "edad": 36,
    "colores": ["Rojo", "Verde", "Azul"],
    "dictionary": { # => diccionario adentro de otro dicccionario
        "key1": "value1",
        "key2": "value2"
    }
}

print(type(usuario)) # => tipo variable
print(usuario) # => mostrar usuario

print(usuario["nombre"]) # salida John                   => mostrar un atributo especifico

print(usuario["colores"]) #=> mostrar atributo del usuario

print(len(usuario["colores"])) # => longitud del array colores, atributo del usuario

print(len(usuario))# => longitud del diccionario

# crear un dic de otra forma con construct

jugador = dict(equipo="x", salario=30000, equipos= ["1", "2", "3"])

print(jugador) # => mostrar a el jugador
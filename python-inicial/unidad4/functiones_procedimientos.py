'''
Función => Una función siempre devuelve un valor (return)
procediminesto => No devuelve un valor
scope => Es el alcance que tiene una variable dentro del código.
'''
#variable global
name = "Agus"

def func():
    global name #acceder a una variable global
    name = name + " Hola" #variable local de la funcion
    print(name)


func()
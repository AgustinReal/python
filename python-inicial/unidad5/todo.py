import os

runnProgram = True
todoList = []

# Función pra mostrar las opciones del menu
def showMenuOptions():
    print("")
    print("")
    print("Por favor seleccione una opción:")
    print("")
    print("")
    print("1. Crear una tarea")
    print("2. Marcar como realizada una tarea.")
    print("3. Borrar una tarea")
    print("4. Salir")

# FUNCIÓN PARA MOSTRAR TODAS LAS TAREAS
def showTodoList():
    global todoList
    print()
    print()
    print("**********************************")
    for todo in todoList:
        print(f"{todoList.index(todo) + 1}. {todo}") # Mostrar strings con variables, para que esto funcione le tenes que poner una f al principio.
    print("**********************************")
    print()
    print()

# Función para guardar las tareas en la variable "todoList"
def createTodo():
    os.system("cls")
    global todoList
    print("Crear una nueva tarea")
    todo = input("Por favor ingrese el nombre de la tarea: ")
    todoList.append(todo)
    # Mostrar la lista de tareas
    showTodoList()

# Función para marcar una tarea como realizada
def updateTodo():
    global todoList
    print("Actualizar una tarea")
    todoId = int(input("Ingrese el número de la tarea que quiere marcar como hecha: "))
    todoList[todoId - 1] = todoList[todoId - 1] + " ✅"
    showTodoList()

# Función que nos permite borrar una tarea 
def deleteTodo():
    global todoList
    print("Borrar una tarea")
    todoId = int(input("Ingrese el número de la tarea que quiere borrar: "))
    del todoList[todoId - 1]
    showTodoList()

def main():
    global runnProgram
    print(".: WELCOME TO A PYTHON TO DO LIST :.")

    while runnProgram:
        showMenuOptions() # aqui invcacomos la función para mostrar las opciones del menu.
        option = int(input("Ingrese el número de la opción: "))

        match option:
            case 1:
                createTodo()
            case 2:
                updateTodo()
            case 3:
                deleteTodo()    
            case 4:
                print("Hasta luego !!!!")  
                runnProgram = False        
            case _:
                print("Error. Ingrese una opción válida")

if __name__ == '__main__': #Esto para decir que este va ser el archivo principal y se va ejecutar primero.
    main()
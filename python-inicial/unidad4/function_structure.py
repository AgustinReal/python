# Las funciones nos permiten ejecutar varias veces una porción de código.
# parametros => cuando se crea la función
# argumentos => caundo se invoca la función

def fibonacciAux(): # funciones vacias para hacer en el futuro
    pass # Es para decir que se usa mas adelante.

def fibonacci(n):
    """Esta es una función que nos devuelve la seria de fibonacci"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()

#invocamos nuestra función
fibonacci(1000)
fibonacci(2000)
fibonacci(5000)

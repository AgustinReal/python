
def operaciones_matematicas(number1, number2):
    """
        Suma de 2 numeros ingresados por parametros
    """
    suma_resultado = number1 + number2
    resta_resultado = number1 - number2
    multiplicacion_resultado = number1 * number2
    division_resultado = number1 / number2

    return suma_resultado, resta_resultado, \
           multiplicacion_resultado, division_resultado

suma, resta, multiplicacion, division = operaciones_matematicas(20, 33)

print(suma)
print(resta)
print(multiplicacion)
print(division)


print(operaciones_matematicas(20, 33))

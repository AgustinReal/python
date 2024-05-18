

def suma(number1, number2, number4, number6, number3=None, number5=10):# Los argumentos opcionales van a lo ultimo
    if number3 is not None:
        print(number1 + number2 + number3)
    else:
        print(number1 + number2)

suma(number1=2, number2=3)
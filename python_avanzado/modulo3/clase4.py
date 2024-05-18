name = "César"
age = 30
print(f"mi nombre es {name} y tengo {age} años")
print("mi nombre es {} y tengo {} años".format(name, age+10))


sql_insert = "insert into users(name, email) values ('{}', '{}')".format(name, age)
print(sql_insert)

print("Nombre: {1}, Edad : {0}". format(age, name))

#print con parametros
producto = "Celular Iphone 12"
precio = 599.99

print("Producto: {prod}, Precio : {pre}".format(prod= producto, pre= precio))

precio = 599

#Para indicar que 599 va ser un float se le pone .2f para castear a float
print("Producto: {prod}, Precio : {pre:.2f}".format(prod= producto, pre= precio)) 

#formatear numeros
num = 12345.6889
print("{:.2f}".format(num))#float con 2 decimales
print("{:,}".format(num))# Numero con . => , (1.000 => 1,000)
print("{:e}".format(num)) # Notación cientifica

#formatear fechas
from datetime import datetime
now = datetime.now()
print("Fecha y hora : {:%d/%m/%Y %H:%M:%S}".format(now))


#alineación y relleno
number = 42
print("Número: {:>10}".format(number)) # Deja espacio
print("Número: {:0<5}".format(number)) # agrega 0 hasta que sea menor a 5 de largo
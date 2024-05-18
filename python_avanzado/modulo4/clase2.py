import decimal

num1 = decimal.Decimal('10.345')
num2 = decimal.Decimal('5.678')

suma = num1 + num2
print("Suma: ", suma)

resta = num1 - num2
print("Resta: ", resta)

multiplicacion = num1 * num2
print("Multiplicación: ", multiplicacion)

division = num1 / num2
print("División: ", division)

#Redondear cantidad de decimales
redondeo_2 = division.quantize(decimal.Decimal("0.00"))
print(redondeo_2)

#Redondear cantidad de decimales para arriba
rendodeo_alza = division.quantize(decimal.Decimal("1.00"), rounding=decimal.ROUND_CEILING)

#Redondear cantidad de decimales para abajo
rendodeo_baja = division.quantize(decimal.Decimal("1.00"), rounding=decimal.ROUND_FLOOR)

#Redondear cantidad de decimales cercano
rendodeo_cercano = division.quantize(decimal.Decimal("1.00"), rounding=decimal.ROUND_HALF_EVEN)

print("Redondeo hacia arriba: ", rendodeo_alza)
print("Redondeo hacia abajo: ", rendodeo_baja)
print("Redondeo cercano: ", rendodeo_cercano)
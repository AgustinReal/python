from geometria import areas
from geometria.perimteros import (
    perimetro_cuadrado,
    perimetro_rectangulo,
    perimetro_circulo
)

area = areas.area_cuadrado(4)
cuadrado_perimetro = perimetro_cuadrado(4)
circulo_perimetro = perimetro_circulo(10)
rectamgulo_perimetro = perimetro_rectangulo(20, 10)

print("AREA DEL CUADRADO: ", area)
print("PERIMETRO DEL CUADRADO: ", cuadrado_perimetro)
print("PERIMETRO DEL CIRCULO: ", round(circulo_perimetro, 2))
print("PERIMETRO DEL RECTANGULO: ", rectamgulo_perimetro)
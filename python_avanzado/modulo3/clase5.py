# Importamos "re" para el manejo de validaciones expresiones reguladres [@, $, etc..(Regex)]
import re 

cadena = "vamos a aprender expresiones regulares con python"

#Para buscar una palabra dentro de un texto y obtener su posición. "parametros": 1er la palabra a buscar . 2do el texto.
busqueda = re.search("aprender", cadena)

print(busqueda)

#busqueda en base a un patrón 
texto = "Lafecha de vencimineto es 2023-12-31 y la fecha de inicio fue 2023-01-15"
# \d numeros de 4 digitos{aclaro los digitos}
patron_fecha = r'\d{4}-\d{2}-\d{2}'

fecha_encontradas = re.findall(patron_fecha, texto)

print(fecha_encontradas)

#reemplazo de texto basado em átrones
texto = "El número de telefono es 001-376-1234"

patron_numero = r'\d{3}-\d{3}-\d{4}'
nuevo_texto = re.sub(patron_numero, '####', texto)

print(nuevo_texto)


#Extracción de urls de un html
html = '<p>Enlace uno <a href="http://www.google.com">Enlace 1</a>'
patron_url = r'<a href="(.*?)">(.*?)</a>'
enlaces = re.findall(patron_url, html)

for enlace in enlaces:
    url,texto = enlace
    print(f"URL : {url}, texto : {texto}")
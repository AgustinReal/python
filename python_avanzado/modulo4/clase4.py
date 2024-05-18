import datetime

fehca_hora_actual =datetime.datetime.now()

print("Fecha y hora actual: ", fehca_hora_actual)

#Formatear una fecha y hora
formato = "%d/%m/%Y %H:%M:%S"
#Segun el formato que quieras, se lo tenes que pasar por parametro a la función "strftime()" 
fecha_formato = fehca_hora_actual.strftime(formato)
print("Fecha formateada: ", fecha_formato)

#Fecha especifica
fecha_especifica = datetime.datetime(2022, 8, 12, 15, 30, 0)
print("Fecha y hora especifica : ", fecha_especifica.strftime(formato))

#calculos con fechas
hoy = datetime.date.today()
tomorrow = hoy + datetime.timedelta(days=1)
diff_dates = tomorrow - hoy
print("Mañana es: ", tomorrow)
print("Faltan ", diff_dates)

#zonas horarias
import pytz 

zona_horraia = pytz.timezone("America/New_York")
fecha_hora_actual = datetime.datetime.now(zona_horraia)
print("Fecha y hora en New York: ", fecha_hora_actual)

#convertir string a fecha
fecha_string = "2023-07-12 18:30:00"
fecha_objeto = datetime.datetime.strptime(fecha_string, "%Y-%m-%d %H:%M:%S")
print("Fecha y hora convertida", fecha_objeto)
print(type(fecha_objeto))
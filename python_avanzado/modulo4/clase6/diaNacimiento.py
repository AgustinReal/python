import datetime

def dia_nacimiento(fecha_nacimineto):
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    index_dia = fecha_nacimineto.weekday()
    return dias[index_dia]

if __name__ == "__main__":
    fecha_string = input("Ingrese Fecha nacimineto (YYYY-MM-DD)")
    fecha_objeto = datetime.datetime.strptime(fecha_string, "%Y-%m-%d")
    dia = dia_nacimiento(fecha_objeto)
    print(f"Naciste un {dia}")
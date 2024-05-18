"""
try: evalua una porción de código
except: manejamos el posible error.
else: se ejecuta cuando no hay un error
finally: Se ejecuta independientemente de si hay o no errores.
"""

try:
    print("hola")
except Exception:
    print("Hubo un error")
else:
    print("No hubo error")
finally:
    print("Esto siempre se ejecuta")

try:
    raise Exception("Error a proposito") #lanzar un error, esto rompe el code y no se ejecuta lo que esta debajo de esto.
    print("agus")
except Exception:
    print("Hubo un error")
else:
    print("No hubo error")
finally:
    print("Esto siempre se ejecuta")
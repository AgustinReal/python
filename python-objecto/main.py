# ejemplo de clase
class Usuario():
    #atributos

    #Contructror
    def __init__(self, nombre, apellido, correo, contrasenia, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasenia = contrasenia
        self.telefono = telefono

    #Metodos
    # Simpre poner como parametro Self para indentificar que es un metódo de clase o si no tira error.
    def encriptarContrasenia(self):
        return "encriptando..."

    def verificarContrassenia(self):
        return "desencriptando"

#instancia de clases
usuario1 = Usuario(
    nombre="Agustin", 
    apellido="real", 
    correo="agustinreal26", 
    contrasenia="aaa", 
    telefono="1152781282"
)

print("Usuario #1")
print(usuario1.nombre)
print(usuario1.apellido)

print("Usuario #2")
usuario2 = Usuario(nombre="trayro", apellido="bell", correo="agustinreal26", contrasenia="aaa", telefono="1152781282")

print(usuario2.nombre)
print(usuario2.apellido)
print(usuario2.encriptarContrasenia())
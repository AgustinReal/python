class Usuario:
     def __init__(self, nombre, apellido, correo, contrasenia, telefono):
          # atributos publicos
          self.nombre= nombre
          self.apellido= apellido
          self.correo= correo
          self.contrasenia= self.EncriptarContrasenia(contrasenia)
          # atributos privados __ => haces que el atributo sea privado.
          self.__telefono= telefono

     def Obtener_telefono(self):
        return self.__telefono
     
     def Actualizar_telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono

     def EncriptarContrasenia(self, contrasenia):
        pass
     
     def VerificarContrasenia(self, contrasenia):
        pass
     
usuario1 = Usuario(nombre="Agustin", apellido="Real", correo="Agus@gmail.com", contrasenia="test", telefono=1234)

print(usuario1.Obtener_telefono())

usuario1.Actualizar_telefono(111111)

print(usuario1.Obtener_telefono())
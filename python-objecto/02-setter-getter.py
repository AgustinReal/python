class Usuario:
     def __init__(self, nombre, apellido, contrasenia):
          # atributos publicos
          self._nombre= nombre #Cuando tiene _ es para indicar que ese atributo va a tener un get y un set.
          self._apellido= apellido
          self._contrasenia= self.EncriptarContrasenia(contrasenia)
        
     def EncriptarContrasenia(self, contrasenia):
        pass
     
     def VerificarContrasenia(self, contrasenia):
        pass
     
     #Getter
     @property #decorador
     def nombre(self):
        return self._nombre
     
     #Setter
     @nombre.setter #decorador
     def nombre(self, nombre):
        self._nombre = nombre

    #Getter
     @property #decorador
     def apellido(self):
        return self._apellido
     
     #Setter
     @apellido.setter #decorador
     def apellido(self, apellido):
        self._apellido = apellido

usuario1 = Usuario("Agus", "Real", "test")

print(usuario1.nombre)
print(usuario1.apellido)

usuario1.nombre = "pala"

print(usuario1.nombre)

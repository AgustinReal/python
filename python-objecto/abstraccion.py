# py -m venv venv => esto para trabajar con un entorno virtual (En este caso para usar abstraccion).
# activar El script => .\venv\Scripts\activate.bat
# pip install crytocode


from cryptocode import encrypt, decrypt
from abc import ABC, abstractmethod

class UsuarioBase(ABC):

    def __init__(self, nombre, apellido, correo, contrasenia, telefono): 
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasenia = self.encriptarContrasenia(contrasenia)
        self.telefono = telefono

    @abstractmethod # decorador
    def encriptarContrasenia(self, contrasenia):
        pass

    @abstractmethod # decorador
    def verificarContrasenia(self, contrasenia):
        pass

class UsuarioConcreto(UsuarioBase):

    def encriptarContrasenia(self, contrasenia):
        return encrypt(contrasenia, "secret")
    
    def verificarContrasenia(self, contrasenia):
        contrasenia_desencriptada =  decrypt(self.contrasenia, "secret")
        return contrasenia_desencriptada == contrasenia, contrasenia_desencriptada
    
usuario1 = UsuarioConcreto(nombre="agus", apellido="real", correo="agus@gmial.com", contrasenia="test", telefono=1111111)

print(usuario1.contrasenia)
esIgual, verContra = usuario1.verificarContrasenia("test")
print(esIgual)
print(verContra)
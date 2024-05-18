class MainMenu:
    # para el uso del menu principal
    @staticmethod #decorador
    def showMainMenu():
        print("*******************************************************************")
        print("AGUS - CONCTACOS BOCA")
        print("*******************************************************************")
        print("1. Añadir contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Cerrar aplicación")
        optiom = int(input("Seleccione una opción: "))
        while optiom > 5 or optiom < 1:
            print("Opcion no valida")
            optiom = int(input("Seleccione una opción: "))
        else:
            return optiom
        
    @staticmethod #decorador
    def showMenuAddContact():
        print("*******************************************************************")
        print("AÑADIR CONTACTO")
        print("*******************************************************************")

    @staticmethod #decorador
    def addContact():
        name = input("Ingrese el nombre: ")
        email = input("Ingrese el email: ")
        phone = int(input("Ingrese el phone: "))
        return name, email, phone
    
    @staticmethod #decorador
    def showMenuAlllContacts():
        print("*******************************************************************")
        print("                        LISTA DE CONTACTOS                         ")
        print("*******************************************************************")
        print("NOMBRE           |             CORREO       |       TELEFONO       ")

    @staticmethod #decorador
    def showMenuSearchContact():
        print("*******************************************************************")
        print("                        BUSCA CONTACTO                             ")
        print("*******************************************************************")

    @staticmethod #decorador
    def searchContact():
        email = input("Ingrese correo de contatco: ")
        return email
    
    @staticmethod #decorador
    def showMenuUpdate():
        print("*******************************************************************")
        print("                        EDITAR CONTACTO                            ")
        print("*******************************************************************")

    @staticmethod #decorador
    def getContactEmail():
        return input("Ingrese correo de contacto: ")
    
    @staticmethod #decorador
    def getContactData():
        name = input("Ingrese nombre de contacto: ")
        phone = input("Ingrese telefono de contacto: ")
        return name, phone
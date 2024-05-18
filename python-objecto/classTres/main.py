from contacts import Contacts
from menu import MainMenu

if __name__ == '__main__':
    while True:
        option = MainMenu.showMainMenu() #muestra el menu principal
        contacts = Contacts()
        match(option):
            case 1: # add contact
                MainMenu.showMenuAddContact()
                name, email, phone = MainMenu.addContact()
                contacts.add(name, email, phone)
                pass
            case 2: # contact list
                MainMenu.showMenuAlllContacts()
                contacts.show_all_contactc()
                pass
            case 3: # search contact
                MainMenu.showMenuSearchContact()
                email = MainMenu.searchContact()
                contact = contacts.search(email)
                if contact:
                    print(contact)
                else:
                    print("El contacto no existe")
                pass
            case 4: # update list
                MainMenu.showMenuUpdate()
                MainMenu.showMenuAlllContacts
                email = contacts.show_all_contactc()
                contact = contacts.search(email)
                if contact:
                    name, phone = MainMenu.getContactData()
                    resp = contacts.update(contact["email"], name, phone)
                    print("Contacto actualizado")
                pass
            case 5: # close app
                print("Hasta luego")
                pass
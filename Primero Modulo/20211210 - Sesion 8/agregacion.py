#agregacion

class Contacto:
    pass

class Agenda: 

    def __init__(self, contactos = []) -> None:
        self.__contactos = contactos

c1 = Contacto()
c2 = Contacto()
c3 = Contacto()

lista = [c1, c2, c3]

agenda = Agenda(lista)

#composicion
class Contacto:
    pass

class Agenda: 

    def __init__(self) -> None:
        self.__contactos = []
    
    def agregar_contacto(self, contacto: Contacto):
        self.__contactos.append(contacto)

c1 = Contacto()
c2 = Contacto()

agenda = Agenda()
agenda.agregar_contacto(c1)
agenda.agregar_contacto(c2)
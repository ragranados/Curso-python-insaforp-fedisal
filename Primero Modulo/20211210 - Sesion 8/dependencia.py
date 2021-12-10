class Documento:

    def __init__(self, texto) -> None:
        self.__texto = texto

    def get_texto(self):
        return self.__texto

class Impresora:

    def imprimir(self, doc: Documento):
        pass
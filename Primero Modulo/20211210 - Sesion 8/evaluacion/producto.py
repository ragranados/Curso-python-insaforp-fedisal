class Producto:

    def __init__(self, nombre_producto: str, precio: float, cantidad: int) ->  None:
        self.__nombre_producto = nombre_producto
        self.__precio = precio
        self.__cantidad = cantidad
    
    def __str__(self) ->  str:
        return f'Nombre: {self.__nombre_producto}\nPrecio: {self.__precio}\nCantidad: {self.__cantidad}'


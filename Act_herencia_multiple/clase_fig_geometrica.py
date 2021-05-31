class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho

    def get_alto(self):
        return self.__alto

    def set_titular(self, alto):
        self.__alto = alto

    def get_ancho(self):
        return self.__ancho

    def set_cantidad(self, ancho):
        self.__ancho = ancho

    def __str__(self):
        return f"Alto: {self.__alto}cm, Ancho: {self.__ancho}cm"


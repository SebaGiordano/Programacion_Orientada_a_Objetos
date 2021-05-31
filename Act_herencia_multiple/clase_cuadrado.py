from Analista_de_Sistemas_2do.POO.Act_herencia_multiple.clase_fig_geometrica import FiguraGeometrica
from Analista_de_Sistemas_2do.POO.Act_herencia_multiple.clase_color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def calcular_area(self):
        if self.get_alto() == self.get_ancho():
            return self.get_alto() * self.get_ancho()
        else:
            return 'No se puede calcular el area del cuadrado porque sus lados no son iguales!'

    def __str__(self):
        return str(FiguraGeometrica.__str__(self)) + ', Color: ' + Color.get_color(self) + ', Area del cuadrado: ' + str(self.calcular_area())+'cm^2'


mi_cuadrado = Cuadrado(12, 12, 'blanco')
mi_cuadrado.calcular_area()
print(mi_cuadrado)




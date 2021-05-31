from Analista_de_Sistemas_2do.POO.Act_herencia_multiple.clase_fig_geometrica import FiguraGeometrica
from Analista_de_Sistemas_2do.POO.Act_herencia_multiple.clase_color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def calcular_area(self):
        if self.get_alto() != self.get_ancho():
            area_rectangulo = self.get_alto() * self.get_ancho()
            return str(area_rectangulo) + 'cm^2'
        else:
            return 'No se puede calcular el area del rectangulo porque sus lados son iguales!'

    def __str__(self):
        return str(FiguraGeometrica.__str__(self)) + ', Color: ' + Color.get_color(self) + ', Area del rectangulo: ' + self.calcular_area()


mi_rectangulo = Cuadrado(12, 16, 'negro')
mi_rectangulo.calcular_area()
print(mi_rectangulo)
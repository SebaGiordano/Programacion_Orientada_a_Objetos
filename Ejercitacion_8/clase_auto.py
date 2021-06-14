from Analista_de_Sistemas_2do.POO.Ejercitacion_8.clase_vehiculo import Vehiculo


class Auto(Vehiculo):
    def __init__(self, marca, cantidad_de_ruedas, tipo_de_combustible, velocidad_maxima,
                 cantidad_de_puertas=int, color=str):
        Vehiculo.__init__(self, marca, cantidad_de_ruedas, tipo_de_combustible, velocidad_maxima)
        self._cantidad_de_puertas = cantidad_de_puertas
        self._color = color

    @property
    def cantidad_de_puertas(self):
        return self._cantidad_de_puertas

    @cantidad_de_puertas.setter
    def cantidad_de_puertas(self, cantidad_de_puertas):
        self._cantidad_de_puertas = cantidad_de_puertas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def realizarMantenimiento(self):
        return (self.cantidad_de_puertas + self.cantidad_de_ruedas) * 35

    def __str__(self):
        return f'{Vehiculo.__str__(self)}' \
               f', Cantidad de puertas: {self.cantidad_de_puertas}' \
               f', Color: {self.color}'

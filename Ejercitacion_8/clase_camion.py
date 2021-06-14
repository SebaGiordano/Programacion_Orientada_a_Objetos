from Analista_de_Sistemas_2do.POO.Ejercitacion_8.clase_vehiculo import Vehiculo


class Camion(Vehiculo):
    def __init__(self, marca, cantidad_de_ruedas, tipo_de_combustible, velocidad_maxima, tipo=str):
        Vehiculo.__init__(self, marca, cantidad_de_ruedas, tipo_de_combustible, velocidad_maxima)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def realizarMantenimiento(self):
        if self.tipo == 'semi':
            return self.velocidad_maxima * 40
        elif self.tipo == 'acoplado':
            return self.velocidad_maxima * 60

    def __str__(self):
        return f'{Vehiculo.__str__(self)}' \
               f', Tipo: {self.tipo}'


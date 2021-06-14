from Analista_de_Sistemas_2do.POO.Ejercitacion_8.clase_vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, marca, cantidad_de_ruedas, tipo_de_combustible, velocidad_maxima,
                 espejoRetrovisor=bool, tipo=str):
        Vehiculo.__init__(self, marca, cantidad_de_ruedas, tipo_de_combustible, velocidad_maxima)
        self._espejoRetrovisor = espejoRetrovisor
        self._tipo = tipo

    @property
    def espejoRetrovisor(self):
        return self._espejoRetrovisor

    @espejoRetrovisor.setter
    def espejoRetrovisor(self, espejoRetrovisor):
        self._espejoRetrovisor = espejoRetrovisor

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def realizarMantenimiento(self):
        return self.velocidad_maxima * 10

    def tiene_espejo_retrovisor(self):
        self._espejoRetrovisor = input("Tiene Espejo Retrovisor? [SI / NO]: ")
        if self._espejoRetrovisor == 'si' or 'SI':
            return True
        elif self._espejoRetrovisor == 'no' or 'NO':
            return False

    def __str__(self):
        return f'{Vehiculo.__str__(self)}' \
               f', Espejo retrovisor: {self.tiene_espejo_retrovisor()}' \
               f', Tipo: {self.tipo}'

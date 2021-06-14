from abc import abstractmethod, ABC


class Vehiculo(ABC):
    def __init__(self, marca=str, cantidad_de_ruedas=int, tipo_de_combustible=str,
                 velocidad_maxima=float):
        self._marca = marca
        self._cantidad_de_ruedas = cantidad_de_ruedas
        self._tipo_de_combustible = tipo_de_combustible
        self._velocidad_maxima = velocidad_maxima

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def cantidad_de_ruedas(self):
        return self._cantidad_de_ruedas

    @cantidad_de_ruedas.setter
    def cantidad_de_ruedas(self, cantidad_de_ruedas):
        self._cantidad_de_ruedas = cantidad_de_ruedas

    @property
    def tipo_de_combustible(self):
        return self._tipo_de_combustible

    @tipo_de_combustible.setter
    def tipo_de_combustible(self, tipo_de_combustible):
        self._tipo_de_combustible = tipo_de_combustible

    @property
    def velocidad_maxima(self):
        return self._velocidad_maxima

    @velocidad_maxima.setter
    def velocidad_maxima(self, velocidad_maxima):
        self._velocidad_maxima = velocidad_maxima

    def __str__(self):
        return f'Marca: {self._marca}' \
               f', Cantidad de ruedas: {self._cantidad_de_ruedas}' \
               f', Tipo de combustible: {self._tipo_de_combustible}' \
               f', Velocidad maxima: {self._velocidad_maxima} km/hs'

    @abstractmethod
    def realizarMantenimiento(self):
        pass

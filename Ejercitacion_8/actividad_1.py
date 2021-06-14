'''
Se solicita que se creen las siguientes clases:

- Vehículo: Que tiene los atributos marca (String), cantidad de ruedas (int), tipo de combustible
(String) y velocidad máxima (double). Método abstracto "realizarMantenimiento": que debe
devolver la cantidad de km en el cuál debe realizar su primer mantenimiento.
- Moto: Que tiene los atributos espejoRetrovisor (boolean) y tipo (String - puede ser
"Todoterreno" o "Ciudad").
- Auto: Que tiene los atributos cantidad de puertas (int) y color (String).
- Camion: Que tiene el atributo tipo (String - puede ser "Semi" o "Acoplado").


Los métodos que debe implementar son:
- Constructor
- Getters y Setters
- Método __str__
- realizarMantenimiento:
* Para el caso de las motos el mantenimiento debe realizarse al km obtenido de multiplicar
la velocidad máxima por 10.
* Para el caso de los autos el mantenimiento debe realizarse al km obtenido de sumar la
cantidad de puertas y la cantidad de ruedas, y eso multiplicado por 35.
* Para el caso de los camiones el mantenimiento debe realizarse al km obtenido de multiplicar
la velocidad máxima por 40 si es "Semi" y por 60 si es "Acoplado".


Finalmente, se debe hacer un menú con una lista de vehículos que coleccione los 3 tipos
de vehículos, con opciones de creación de vehículos, mostrar los datos de los vehículos, y
realizar el mantenimiento de los mismos.
'''
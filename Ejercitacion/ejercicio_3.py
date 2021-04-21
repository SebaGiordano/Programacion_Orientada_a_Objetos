'''
3- Área de un triángulo

Desarrolle un programa para calcular el área de un triángulo, cargando por teclado
el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base.
(Observar que la altura no es un dato… sólo se indica la forma de calcularla
de acuerdo a la base que sí es un dato).
'''

print(">>>>> AREA DE UN TRIANGULO <<<<<\n")
base = int(input("Ingrese la base del triangulo: "))
altura = (base**2)
print(f"\nEn base a las reglas del enunciado, la altura del triangulo es {altura}")
area_del_triangulo = (base*altura/2)
print(f"\nPor correspondencia, el area del triangulo es: {area_del_triangulo}")

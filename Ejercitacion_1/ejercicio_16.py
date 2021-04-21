'''
16- Datos de un rectángulo

Hacer un programa que tome como entrada el ancho y el alto de un rectángulo y determine el
perímetro y la superficie del mismo.
'''

ancho = int(input("Digite el ancho de un rectangulo: "))
alto = int(input("Digite el alto de un rectangulo: "))
perimetro = 2*(ancho+alto)
superficie = ancho*alto
print(f"\nEl perimetro del rectangulo es: {perimetro}")
print(f"La superficie del rectangulo es: {superficie}m2")
'''
8- Cuadrados y cubos
Leer dos números y calcular:
La suma de sus cuadrados.
El promedio de sus cubos.
'''

a = int(input("Ingrese un valor: "))
b = int(input("Ingrese otro valor: "))

suma_cuadrados = (a**2+b**2)
promedio_cubos = (a**3+b**3/2)

print(f"\nLa suma de sus cuadrados es igual a: {suma_cuadrados}")
print(f"Ll promedio de sus cubos es igual a: {promedio_cubos}")

'''
1. Suma - División - Potencia

Se necesita desarrollar un programa que permita calcular la suma de tres números.
Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales),
en caso contrario elevar el resultado al cubo.
'''

print("Debera ingresar 3 numeros enteros")

acum = 0

for i in range(0,3):
    num = input(f"Numero {i+1}: ")
    acum = acum + int(num)

if acum > 10:
    print("La suma de los tres numeros ingresados es mayor a 10")
    division = acum / 2
    print(f"El resutado de dividir {acum} en 2, es: {division:.0f}")
else:
    cubo = acum ** 3
    print("La suma de los tres numeros ingresados es menor a 10")
    print(f"El resutado de elevar {acum} al cubo, es: {cubo}")





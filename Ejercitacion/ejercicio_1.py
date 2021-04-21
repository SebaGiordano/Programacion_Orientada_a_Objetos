'''
1- División con resto

Plantear un script que permita informar, para dos valores a y b el resultado
de la división a/b y el resto de esa división.
'''

print("Debera ingresar 2 valores!\n")
a = int(input("Valor 'A': "))
b = int(input("Valor 'B': "))
resultado1 = a / b
print(f"\n>>> El resultado de dividir {a} en {b} es, {resultado1}\n")
resultado2 = a % b
print(f">>> El resto de dividir {a} en {b} es, {resultado2}")



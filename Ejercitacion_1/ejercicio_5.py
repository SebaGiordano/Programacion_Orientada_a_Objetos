'''
5- Conversión de medidas

Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:

•	yardas
•	pulgadas
•	centímetros
•	metros

Sabiendo que:

•	1 pie = 12 pulgadas
•	1 yarda = 3 pies
•	1 pulgada = 2.54 centímetros
•	1 metro = 100 centímetros
'''

a = int(input("Ingrese una cantidad dada de pies: "))
yardas = a/3
print(f"\n{a} pies, equivalen a {yardas} yardas")
pulgadas = a*12
print(f"{a} pies, equivalen a {pulgadas} pulgadas")
centimetros = pulgadas*2.54
print(f"{a} pies, equivalen a {centimetros} centimetros")
metros = centimetros/100
print(f"{a} pies, equivalen a {metros} metros")

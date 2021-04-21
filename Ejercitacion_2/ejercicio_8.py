'''
8. Operaciones de orden con tres números
Realizar un programa que tome tres números, los ordene de mayor a menor,
y diga si el tercero es el resto de la división de los dos primeros.
'''

print("Debera ingresar 3 numeros\n")
lista = []
for i in range(0, 3):
    num = input(f"Numero {i+1}: ")
    lista.append(num)

print(f"\nLos tres numeros ingresados son: {lista}\n")

lista.sort()
lista.reverse()

print(f"Ordenados de Mayor a Menor: {lista}")

division_dos_primeros = int(lista[0]) / int(lista[1])
print(f"\nEl resultado de dividir los 2 primeros numeros es: {division_dos_primeros:.2f}\n")

resto_division = division_dos_primeros % 1

if resto_division == lista[2]:
    print(f"El resto de la division de los 2 primeros numeros es {resto_division:.2f}\n"
          "Por lo tanto, el tercer numero es el resto de la división de los dos primeros")
else:
    print(f"El resto de la division de los 2 primeros numeros es {resto_division:.2f}\n"
          "Por lo tanto, el tercer numero no es el resto de la división de los dos primeros")

'''
11- Polinomio de segundo grado

Desarrollar un programa que cargue por teclado los coeficientes a, b y c
de un polinomio de segundo grado, y calcule y muestre el valor del polinomio
en el punto x (cargando también x por teclado).
Además, para el mismo polinomio, calcule y muestre el valor del discriminante
de la fórmula para el cálculo de las raíces de la ecuación.  
'''

a = int(input(f"Ingrese el valor del coeficiente A para el polinomio de segundo grado: "))
b = int(input(f"Ingrese el valor del coeficiente B para el polinomio de segundo grado: "))
c = int(input(f"Ingrese el valor del coeficiente C para el polinomio de segundo grado: "))
x = int(input(f"Ingrese el valor de X para el polinomio de segundo grado: "))

valor_polinomio_en_x = (a*(x**2)) + b*x + c

print(f"El valor del polinomio cuando X es igual a {x} es: {valor_polinomio_en_x}")

valor_discriminante = b**2 - 4*a*c

print(f"El valor del discriminante para el cálculo de las raíces es: {valor_discriminante}")
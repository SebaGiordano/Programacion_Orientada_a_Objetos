'''
12- Cálculo de ángulos

Se sabe que la suma de dos ángulos desconocidos (𝛼+𝛽) es igual a cierto
valor 𝑥 que se carga por teclado. Además se sabe que la diferencia entre esos
mismos dos ángulos (𝛼 − 𝛽) es igual a otro valor 𝑦 que también se carga por teclado.
Desarrolle un programa que dados los valores 𝑥 e 𝑦, determine el valor de los dos
ángulos 𝛼 y 𝛽. No es necesario convertir a grados, minutos y segundos el valor de
cada ángulo: expréselos como números reales, tal cual hayan sido obtenidos.
'''

x = int(input("Ingrese el valor de X: "))
y = int(input("Ingrese el valor de Y: "))

# Ecuaciones de ángulos:
# a + b = x
# a - b = y

# Sustitución
# Despejo a en a+b=x ==> a=x-b
# Reemplazo a en a-b=y ==> (x-b) - b = y
# Despejo B en la ecuación obtenida:
# -2b= y-x
# b = (y-x)/-2

# Reemplazo valores de X e Y por los introducidos por usuario para calcular el valor de B:

b = (y-x)/-2

print(f"\nEl valor del ángulo B es igual a: {b}")

#Despejo A en una de las primeras ecuaciones: a-b=y ==> a=b+y

#Reemplazo B e Y en la ecuación obtenida para calcular el valor de A:

a = b+y

print(f"El valor del ángulo A es igual a: {a}")

#Verifico en ambas ecuaciones iniciales para ver si A y B están bien calculados:

print(f"\nVerifico en ecuación a + b = x: "
      f"\n{a+b} es igual a: {x}")

print(f"Verifico en ecuación a - b = y: "
      f"\n{a-b} es igual a: {y}")
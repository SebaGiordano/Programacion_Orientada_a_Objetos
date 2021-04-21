'''
2- Cuadrado de un binomio

Plantear un script, que permita mostrar, para dos valores 𝑎 y 𝑏, que:
Un binomio al cuadrado (suma) es igual al cuadrado del primer término, más
el doble producto delprimero por el segundo más el cuadrado del segundo
'''

print("Debera ingresar 2 valores!\n")
a = int(input("Valor 'A': "))
b = int(input("Valor 'B': "))
resultado2 = ((a+b)**2)
resultado = (a**2+2*a*b+b**2)
print(f"\n>>> El resultado de un binomio al cuadrado es: {resultado2}")
print(f"\n>>> El resultado del cuadrado del primer término, más el doble producto "
      f"del primero por el segundo más el cuadrado del segun,es igual a: {resultado}\n")
print("Se puede apreciar que ambos resultados son iguales")

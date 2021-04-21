'''
4- Últimos dígitos

¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número
entero?
¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número
entero por teclado, y muestre el último dígito del mismo (por un lado) y los dos
últimos dígitos (por otro lado)
[Ayuda: ¿Cuáles son los posibles restos que se obtienen de dividir un número
cualquiera por 10?]
'''
'''
¿Cómo usaría el operador resto (%) para obtener el valor del último dígito
de un número entero?
> Podemos obtener el último dígito de un numero mediante la operación módulo (%)
con el número 10. Es decir, el resto de dividir a un número por 10 siempre
dará lugar al último dígito de dicho número..
'''

a = int(input("Ingrese un numero entero: "))
ultimo_digito = (a % 10)
ultimos_2_digitos = (a % 100)
print(f"\nEl ultimo digito de {a}, es {ultimo_digito}!")
print(f"Los ultimos 2 digitos de {a}, es {ultimos_2_digitos}!")
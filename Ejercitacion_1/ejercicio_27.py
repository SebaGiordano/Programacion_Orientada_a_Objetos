'''
27- Palabra enmascarada
Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva
enmascarada, mostrando la primer letra y la última, pero reemplazando los caracteres
intermedios por asteriscos.
Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.
'''

palabra = str(input("Ingrese una palabra cualquiera para que sea devuelta de forma enmascarada: "))

asteriscos = str('*'*(len(palabra)-2))

palabra_enmascarada = palabra[0] + asteriscos + palabra[-1]

print(f"La palabra que introdujo de forma enmascarada es: {palabra_enmascarada}")

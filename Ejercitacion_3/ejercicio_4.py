'''
4. Análisis de texto
Se solicita crear un programa que permita ingresar un texto, las palabras se encontraran
separadas únicamente por espacios en blanco y el mismo debe finalizar con un punto.
En base a ese texto determinar:

• La cantidad de palabras que comienzan y terminan en vocal
• La cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior
• El porcentaje que representa el punto a. sobre el total de palabras del texto
Por ejemplo, si el texto ingresado es “Esto es solo una prueba algorítmica.”,
la salida esperada es la siguiente:

Hay 4 palabras que empiezan y terminan en vocales que
representan el 66.67 % de palabras del texto
Hay 2 palabras que comienzan con el último caracter
de la palabra anterior
'''

import re

texto_a_analizar = input(f"Ingrese el texto que desea analizar, finalizado por un punto: ")

contador_palabras_comenzadas_en_vocal = 0
contador_palabras_terminadas_en_vocal = 0
caracter_anterior = ''

vocales = ['a', 'e', 'i', 'o', 'u']

for caracter in texto_a_analizar:
    if caracter == ' ' or caracter == '.':
        if caracter_anterior in vocales:
            contador_palabras_terminadas_en_vocal += 1
    caracter_anterior = caracter

vocales = r'\b[aeiou]\w+\b'
resultado = re.findall(vocales, texto_a_analizar)

for i in resultado:
    contador_palabras_comenzadas_en_vocal += 1

#print(f"La cantidad de palabras que comienzan con vocales en el texto ingresado, "
      #f"es igual a: {contador_palabras_comenzadas_en_vocal}, y la cantidad de"
      #f"palabras que termianan en vocal, es igual a: {contador_palabras_terminadas_en_vocal}\n")

cantidad_de_palabras_que_empiezan_y_termianan_con_vocales = 0
vocales = r'\b[aeiou]\w+[aeiou$]\b'
resultado = re.findall(vocales, texto_a_analizar)

for i in resultado:
    cantidad_de_palabras_que_empiezan_y_termianan_con_vocales += 1

#print(f"La cantidad de palabras que empiezan y termianan con vocales, es: {cantidad_de_palabras_que_empiezan_y_termianan_con_vocales} palabras\n")

cant_espacios = 0

for i in texto_a_analizar:
    if i == ' ':
        cant_espacios = (cant_espacios + 1)
cant_palabras = cant_espacios + 1

porcentaje_de_palabras_que_empiezan_y_terminan_con_vocales = (cantidad_de_palabras_que_empiezan_y_termianan_con_vocales * 100) / cant_palabras

#print(f"Las palabras que empiezan y terminan con vocales representar el {porcentaje_de_palabras_que_empiezan_y_terminan_con_vocales:.0f}% del total de palabras\n")

# OTRA_FORMA_DE_RESOLVERLO:

vocales = 'aeiouAEIOU'

contador_palabras = 0
contador_letras = 0
contador_empieza_vocal = 0
contador_empieza_ultima = 0

empieza_vocal = False

ultimo_caracter_palabra = ''
caracter_anterior = ''

for caracter in texto_a_analizar:
    contador_letras += 1
    if caracter == ' ' or caracter == '.':
        if contador_letras > 0:
            contador_palabras = contador_palabras + 1
            ultimo_caracter_palabra = caracter_anterior
            if empieza_vocal and caracter_anterior in vocales:
                contador_empieza_vocal = contador_empieza_vocal + 1
                empieza_vocal = False

        contador_letras = 0

    elif contador_letras == 1:
        if caracter in vocales:
            empieza_vocal = True
        if ultimo_caracter_palabra == caracter:
            contador_empieza_ultima = contador_empieza_ultima + 1
            ultimo_caracter_palabra = ''

    caracter_anterior = caracter

if contador_palabras > 0:

    #porcentaje = (contador_empieza_vocal * 100) / contador_palabras
    #print(f"\nHay {contador_empieza_vocal} palabras que empiezan y terminan en vocales que "
          #f"representan el {porcentaje:.0f} % de palabras en el texto")

    print(f"\nHay {cantidad_de_palabras_que_empiezan_y_termianan_con_vocales} palabra/as que empieza/an y termina/an en vocal que representan "
          f"el {porcentaje_de_palabras_que_empiezan_y_terminan_con_vocales:.0f}% de palabras del texto\n"
          f"Hay {contador_empieza_ultima} palabra/as que comienza/an con el último caracter "
          f"de la palabra anterior")
else:
    print(f"\nNo se ingresó ningun texto a analizar. Vuelve a intentarlo!!!")

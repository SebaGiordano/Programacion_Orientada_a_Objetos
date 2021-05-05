'''
2- Sílaba 'pe'

Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en
una variable de tipo cadena de caracteres. Se supone que el usuario cargará un punto para indicar el
final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco.
El programa debe:
Determinar cuántas palabras tienen 3, 5 o 7 letras.
Determinar la cantidad de palabras con más de tres letras, que tienen una vocal en la tercera
letra.
Determinar el porcentaje de palabras que tienen sólo una o dos vocales sobre el total de palabras
del texto.
Determinar la cantidad de palabras que contienen más de una vez la sílaba “pe”.

Por ejemplo, si el texto ingresado es “Mi amigo pepe tiene un auto verde.”, la salida esperada es
la siguiente:

La cantidad de palabras con 3, 5 o 7 letras de longitud son: 3
La cantidad de palabras con mas de 3 letras y una vocal en la tercer letra
son: 2
El porcentaje de palabras con 2 vocales sobre el total del texto es: 57.14%
La cantidad de palabras con mas de una sílaba 'pe' es: 1

Utilizar funciones para el desarrollo del programa.
'''


def porcentaje(rangoPalabras1o2Vocales, totalPalabras):
    porcentaje_primer_punto = ((rangoPalabras1o2Vocales * 100) / totalPalabras)
    return porcentaje_primer_punto


def texto_a_ingresar():
    texto = str(input("\nIngrese un texto con espacios entre palabras y finalizado por un punto: "))
    while texto == '':
        print("\nERROR! No ha ingresado ningun texto. Vuelve a intentarlo!")
        texto = str(input("Ingrese un texto con espacios entre palabras y finalizado por un punto: "))
    while (texto[-1] != '.'):
        texto = input("\nERROR!! El texto debe finalizar con un punto. vuelve a intentarlo: ")
        while texto == '':
            print("\nERROR! No ha ingresado ningun texto. Vuelve a intentarlo!")
            texto = str(input("Ingrese un texto con espacios entre palabras y finalizado por un punto: "))
    return texto


def main():
    texto_a_analizar = texto_a_ingresar()

    cant_palabras_con_357 = 0
    cantidad_palabras_3ra_letra_vocal = 0
    cantidad_palabras_con_1o2_vocales = 0
    cantidad_palabras_2omas_silabas_pe = 0

    letra_ant = ""
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"

    cantidad_palabras_silaba_pe = 0
    cantidad_letras_por_palabras_lista = []
    cantidad_vocales_por_palabra_lista = []
    cont_letras = 0
    cantidad_palabras = 0
    cantidad_vocales_por_palabra = 0
    total_letras = 0
    bandera_silaba_pe = True

    for letra in texto_a_analizar:
        total_letras = total_letras + 1
        cont_letras = cont_letras + 1

        if letra in vocales and letra != " " and letra != ".":
            cantidad_vocales_por_palabra = cantidad_vocales_por_palabra + 1

        if letra_ant == "p" and letra == "e" and bandera_silaba_pe == True:
            cantidad_palabras_silaba_pe = cantidad_palabras_silaba_pe + 1

        if cantidad_palabras_silaba_pe == 2 or cantidad_palabras_silaba_pe > 2:
            cantidad_palabras_2omas_silabas_pe = cantidad_palabras_2omas_silabas_pe + 1
            bandera_silaba_pe = False
            cantidad_palabras_silaba_pe = 0

        if letra == " " or letra == ".":
            cantidad_palabras = cantidad_palabras + 1
            cantidad_letras_por_palabra = cont_letras - 1
            cantidad_letras_por_palabras_lista.append(cantidad_letras_por_palabra)
            cantidad_vocales_por_palabra_lista.append(cantidad_vocales_por_palabra)
            cantidad_vocales_por_palabra = 0
            cont_letras = 0

            bandera_silaba_pe = True

        elif cont_letras == 4:
            if letra_ant in vocales:
                cantidad_palabras_3ra_letra_vocal = cantidad_palabras_3ra_letra_vocal + 1

        letra_ant = letra

    for numero in cantidad_letras_por_palabras_lista:
        if numero == 3 or numero == 5 or numero == 7:
            cant_palabras_con_357 = cant_palabras_con_357 + 1

    for numero in cantidad_vocales_por_palabra_lista:
        if numero == 2 or numero == 1:
            cantidad_palabras_con_1o2_vocales = cantidad_palabras_con_1o2_vocales + 1

    print(f"La cantidad de palabras con 3, 5 o 7 letras de longitud son: {cant_palabras_con_357}")
    print(f"La cantidad de palabras con mas de 3 letras y una vocal en la tercer letrac "
          f"son: {cantidad_palabras_3ra_letra_vocal}")
    print(f"El porcentaje de palabras con 1 o 2 vocales sobre el total del texto "
          f"es: {porcentaje(cantidad_palabras_con_1o2_vocales, cantidad_palabras):.2f}% ")
    print(f"La cantidad de palabras con mas de una sílaba 'pe' "
          f"es: {cantidad_palabras_2omas_silabas_pe}")


main()

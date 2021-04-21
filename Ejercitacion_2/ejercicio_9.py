'''
9. Elecciones presidenciales

Según la Ley Electoral de la República Argentina, el Presidente y el Vicepresidente
se eligen de acuerdo a las siguientes reglas:
Artículo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco
por ciento (45 %) de los votos afirmativos válidamente emitidos; en su defecto,
aquella que hubiere obtenido el cuarenta por ciento (40 %) por lo menos de los votos
afirmativos válidamente emitidos y, además, existiere una diferencia mayor de diez
puntos porcentuales respecto del total de los votos afirmativos válidamente emitidos,
sobre la fórmula que le sigue en número de votos.
Artículo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo
al escrutinio ejecutado por las Juntas Electorales, y cuyo resultado único para toda
la Nación será anunciado por la Asamblea Legislativa atento lo dispuesto por el artículo 120
de la presente ley, se realizará una segunda vuelta dentro de los treinta (30) días.
Artículo 151. — En la segunda vuelta participarán solamente las dos fórmulas más votadas
en la primera, resultando electa la que obtenga mayor número de votos afirmativos válidamente
emitidos.

Desarrollar un programa que permita ingresar, para los 3 partidos más votados:
fórmula (presidente + vice) y cantidad de votos obtenidos.

Luego determinar:

• Qué fórmula obtuvo el mayor porcentaje.
• Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso,
indicar también quienes participan de la segunda vuelta
'''

print("Debera ingresar los 3 partidos seleccionados\n")

total_votos = 0
lista_presidente = []
lista_vice = []
lista_votos = []
lista_balotage = []

for i in range(0, 3):
    print(f"Partido {i+1}")
    presidentes = input("Presidente: ")
    lista_presidente.append(presidentes)
    vicepresidente = input("Vicepresidente: ")
    lista_vice.append(vicepresidente)
    cant_votos = int(input("Votos obtenidos: "))
    lista_votos.append(cant_votos)
    total_votos = total_votos + cant_votos

print(f"\nLa cantidad de votos totales, fue: {total_votos} votos")

porcetaje_partido_1 = ((lista_votos[0] * 100) / total_votos)
porcetaje_partido_2 = ((lista_votos[1] * 100) / total_votos)
porcetaje_partido_3 = ((lista_votos[2] * 100) / total_votos)

porcetaje_partido_1_entero = (round(porcetaje_partido_1, 1))
porcetaje_partido_2_entero = (round(porcetaje_partido_2, 1))
porcetaje_partido_3_entero = (round(porcetaje_partido_3, 1))

p1 = str(porcetaje_partido_1_entero) + '%' + ' ' + '(PARTIDO 1)'
p2 = str(porcetaje_partido_2_entero) + '%' + ' ' + '(PARTIDO 2)'
p3 = str(porcetaje_partido_3_entero) + '%' + ' ' + '(PARTIDO 3)'

lista_balotage = [p1, p2, p3]
lista_balotage.sort(reverse=True)

print("\nPRIMER PARTIDO\n"
      f"Presidente: {lista_presidente[0]}\n"
      f"Vicepresidente: {lista_vice[0]}\n"
      f"Votos obtenidos: {lista_votos[0]}\n"
      f"Porcentaje de votos: {porcetaje_partido_1:.1f}%\n")

print("SEGUNDO PARTIDO\n"
      f"Presidente: {lista_presidente[1]}\n"
      f"Vicepresidente: {lista_vice[1]}\n"
      f"Votos obtenidos: {lista_votos[1]}\n"
      f"Porcentaje de votos: {porcetaje_partido_2:.1f}%\n")

print("TERCER PARTIDO\n"
      f"Presidente: {lista_presidente[2]}\n"
      f"Vicepresidente: {lista_vice[2]}\n"
      f"Votos obtenidos: {lista_votos[2]}\n"
      f"Porcentaje de votos: {porcetaje_partido_3:.1f}%\n")

if porcetaje_partido_1 > porcetaje_partido_2 and porcetaje_partido_1 > porcetaje_partido_3:
    print(f"El primer partido obtuvo la mayor cantidad de votos con un porcentaje "
          f"de {porcetaje_partido_1:.1f}%\n")
    if porcetaje_partido_1 and porcetaje_partido_2 and porcetaje_partido_3 < 40:
        print("Hay segunda vuelta electoral\n")
        print('Los 2 partidos que iran a segunda vuelta electoral son los que obtuvieron el', lista_balotage[0], 'y',
          lista_balotage[1])
    elif porcetaje_partido_1 >= 45:
        print("Formula ganadora por haber obtenido el 45% o mas de la cantidad de votos!")
    elif porcetaje_partido_1 >= 40 <= 44:
        if porcetaje_partido_1 - porcetaje_partido_2 > 10 and porcetaje_partido_1 - porcetaje_partido_3 > 10:
            print("Formula ganadora por obtener el 40% o mas de la cantidad de votos y ademas"
                  "por tener una direncia del 10% con respecto al segundo!")
        else:
            print("El porcentaje de votos iguala o supera el 40% pero no hay una diferencia del 10%"
                  " con respecto al segundo\n"
                  "\nHay egunda vuelta electoral\n")
            print('Los 2 partidos que iran a segunda vuelta electoral son los que obtuvieron el', lista_balotage[0],
                  'y', lista_balotage[1])
elif porcetaje_partido_2 > porcetaje_partido_1 and porcetaje_partido_2 > porcetaje_partido_3:
    print(f"El segundo partido obtuvo la mayor cantidad de votos con un porcentaje "
          f"de {porcetaje_partido_2:.1f}%\n")
    if porcetaje_partido_1 and porcetaje_partido_2 and porcetaje_partido_3 < 40:
        print("Hay segunda vuelta electoral\n")
        print('Los 2 partidos que iran a segunda vuelta electoral son los que obtuvieron el', lista_balotage[0], 'y',
          lista_balotage[1])
    elif porcetaje_partido_2 >= 45:
        print("Formula ganadora por haber obtenido el 45% o mas de la cantidad de votos!")
    elif porcetaje_partido_2 >= 40 <= 44:
        if porcetaje_partido_2 - porcetaje_partido_1 > 10 and porcetaje_partido_2 - porcetaje_partido_3 > 10:
            print("Formula ganadora por obtener el 40% o mas de la cantidad de votos y ademas"
                  "por tener una direncia del 10% con respecto al segundo!")
        else:
            print("El porcentaje de votos iguala o supera el 40% pero no hay una diferencia del 10%"
                  " con respecto al segundo\n"
                  "Hay egunda vuelta electoral\n")
            print('Los 2 partidos que iran a segunda vuelta electoral son los que obtuvieron el', lista_balotage[0],
                  'y', lista_balotage[1])
elif porcetaje_partido_3 > porcetaje_partido_1 and porcetaje_partido_3 > porcetaje_partido_2:
    print(f"El tercer partido obtuvo la mayor cantidad de votos con un porcentaje "
          f"de {porcetaje_partido_3:.1f}%")
    if porcetaje_partido_1 and porcetaje_partido_2 and porcetaje_partido_3 < 40:
        print("Hay segunda vuelta electoral\n")
        print('Los 2 partidos que iran a segunda vuelta electoral son los que obtuvieron el', lista_balotage[0], 'y',
          lista_balotage[1])
    elif porcetaje_partido_3 >= 45:
        print("Formula ganadora por haber obtenido el 45% o mas de la cantidad de votos!")
    elif porcetaje_partido_3 >= 40 <= 44:
        if porcetaje_partido_3 - porcetaje_partido_2 > 10 and porcetaje_partido_3 - porcetaje_partido_1 > 10:
            print("Formula ganadora por obtener el 40% o mas de la cantidad de votos y ademas"
                  "por tener una direncia del 10% con respecto al segundo!")
        else:
            print("El porcentaje de votos iguala o supera el 40% pero no hay una diferencia del 10%"
                  " con respecto al segundo\n"
                  "Hay segunda vuelta electoral\n")
            print('Los 2 partidos que iran a segunda vuelta electoral son los que obtuvieron el', lista_balotage[0],
                  'y', lista_balotage[1])
else:
    print("Las tres formulas obtuvieron los mismos procentajes de votos")

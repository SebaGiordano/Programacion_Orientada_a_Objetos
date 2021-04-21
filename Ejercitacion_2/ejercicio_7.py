'''
7. Tirada de moneda

Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. Permitir que un
jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta.
'''

import random

print(">>> TIRADA DE MONEDA <<<\n")
print("Digite '1' si apuesta 'CARA'\n"
      "Digite '2' si apuesta 'CRUZ\n")

apuesta = input("Numero de apuesta: ")

if apuesta == 1:
    apuesta = 'cara'
else:
    apuesta = 'cruz'

caras = ('cara', 'cruz')
resultado_apuesta = (random.choice(caras))

print(f"\nEl jugador aposto por {apuesta}, el resultado de la apuesta fue: {resultado_apuesta}\n")

if apuesta == resultado_apuesta:
    print("Bravo!!! Su apuesta ha sido Satisfactoria")
elif apuesta != resultado_apuesta:
    print("Error!!! Su apuesta ha fallado")

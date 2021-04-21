'''
15- Rinde de un campo agrícola
Un productor agrícola desea saber cuantos quintales de trigo puede producir en su parcela,
por lo tanto, se pide ingresar el largo y el ancho en metros de la parcela y determinar
el rinde sabiendo que en 10 m2 se obtiene 2 quintales.
'''

largo = int(input("\n> Ingrese la cantidad de metros de largo de la parcela: "))
ancho = int(input("> Ingrese la cantidad de metros de ancho de la parcela: "))
m2 = largo*ancho
quintales = m2/10*2
print(f"\nLa cantidad de metros cuadrados de la parcela, es: {m2}m2")
print(f"La cantidad de quintales de trigo que puede producir en la parcela, "
      f"es: {quintales} quintales")

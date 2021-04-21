'''
25- Costos del proyecto
Una pequeña empresa de informática tiene que desarrollar un sistema de información
(a.k.a un super programa) y para ello tiene un presupuesto X para cubrir
los costos de crear el sistema. Sabiendo que tiene pensado ganar al menos 17 %
por el proyecto, determine cual es el valor máximo que pueden alcanzar
los costos del proyecto.
'''

presupuesto = int(input("Ingrese el presupuesto con el que cuenta para crear el sistema: "))

ganancia_minima = (presupuesto*17)/100

costos = presupuesto-ganancia_minima

print(f"Los costos no deben exceder el siguiente importe: ${costos}")

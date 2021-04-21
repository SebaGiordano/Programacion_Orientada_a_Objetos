'''
24- Cálculo distancia de viaje

Una persona cautivada por los paisajes argentinos se le ocurrió la loca idea de
unir los puntos mas extremos (Ushuaia y La Quiaca) en bicicleta, es decir se
propuso hacer 3641.3 Km en bicicleta.
Nuestro aventurero efectivamente inició la travesía pero se accidentó y solo
recorrió X metros según su GPS.
Usted debe solicitar ese valor e informar cuantos kilómetros y metros recorrió
nuestro aventurero y que porcentaje represento lo recorrido del total de km
a recorrer de Ushuaia a La Quiaca (para el porcentaje usted deberá
realizar los cálculos en metros).
'''

metros_recorridos = int(input("Ingrese la cantidad de metros que recorrio el aventurero: "))
km_recorridos = (metros_recorridos/1000)
resto = km_recorridos%1*1000
metros_totales = 3641.3 * 1000
porcentaje_metros_recorridos = metros_recorridos * 100 / metros_totales
print(f"\nEl aventurero ha recorrido {(km_recorridos)-(km_recorridos%1):.0f} km y {resto:.0f} metros\n"
      f"El porcentaje de metros recorridos fue {porcentaje_metros_recorridos:.0f}%")




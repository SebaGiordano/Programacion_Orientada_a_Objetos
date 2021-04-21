'''
20- Duración de un vuelo

Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo
(hora y minutos), determine cuál es su duración en minutos.
Si el viajero necesita luego 45 minutos más para ir del aeropuerto al
hotel que ha reservado, ¿a qué hora llegara al mismo?
'''

partida=input(f"Ingrese el horario de partida del vuelo en formato hh:mm : ")

llegada= input(f"Ingrese el horario de llegada del vuelo en formato hh:mm : ")


hora_partida=partida[0] + partida[1]
hora_partida_int=int(hora_partida)

minutos_partida=  partida[3] + partida[4]
minutos_partida_int=int(minutos_partida)

hora_llegada= llegada[0] + llegada[1]
hora_llegada_int=int(hora_llegada)

minutos_llegada= llegada[3] + llegada[4]
minutos_llegada_int=int(minutos_llegada)

hora_partida_int_a_minutos=hora_partida_int*60

hora_llegada_int_a_minutos= hora_llegada_int*60

minutos_totales_vuelo_partida=minutos_partida_int+hora_partida_int_a_minutos

minutos_totales_vuelo_llegada=minutos_llegada_int+ hora_llegada_int_a_minutos

tiempo_total_viaje=minutos_totales_vuelo_llegada-minutos_totales_vuelo_partida

print(f"El tiempo total del vuelo son: {tiempo_total_viaje} minutos")

minutos_totales_hotel=minutos_totales_vuelo_llegada+45

hora_llegada_hotel=(minutos_totales_hotel/60)

hora_llegada_hotel_str= str(hora_llegada_hotel)
hora_llegada_hotel_real_str=hora_llegada_hotel_str[0] +  hora_llegada_hotel_str[1]

minutos_llegada_hotel= (minutos_totales_hotel%60) #resto para obtener minutos

print(f"El horario de llegada al hotel es: {hora_llegada_hotel_real_str}:{minutos_llegada_hotel} hs")
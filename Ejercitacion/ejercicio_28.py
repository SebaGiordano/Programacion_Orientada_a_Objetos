'''
28- Cálculo de posta de natación

En la disciplina olímpica una de las pruebas mas esperadas es en la natación la posta 4 x 100 estilos.
En esta disciplina el equipo nadador registro los siguientes tiempos en cada estilo:

•	Espalda 52 seg 15 centésimas
•	Pecho 1 minuto 2 segundos 75 centésimas
•	Mariposa 59 segundos 80 centésimas
•	Crol o Libre 48 segundos 15 centésimas

Usted debe averiguar el tiempo total de la carrera del equipo ganador y representarlo en minutos,
segundos y centésimas.
Para recordar:

•	1 minutos son 60 segundos
•	1 segundo son 100 centésimas
'''

espalda = ((52*100)+15)
pecho = ((1*60*100)+(2*100)+75)
mariposa = ((59*100)+80)
crol = ((48*100)+15)

tiempo_total_en_centesimas = espalda + pecho + mariposa + crol

print(f"\nEl tiempo total en centesimas es: {tiempo_total_en_centesimas}")

tiempo_total_en_segundos = (tiempo_total_en_centesimas / 100)
tiempo_total_en_minutos = (tiempo_total_en_segundos / 60)
minutos_totales_entero = (tiempo_total_en_minutos - (tiempo_total_en_minutos%1))
segundos_restantes = (tiempo_total_en_minutos%1)*60
segundos_restantes_entero = (segundos_restantes - (segundos_restantes%1))
centesimas_restantes = ((segundos_restantes%1)*100)

'''
print(tiempo_total_en_segundos)
print(tiempo_total_en_minutos)
print(minutos_totales_entero)
print(segundos_restantes)
print(segundos_restantes_entero)
print(centesimas_restantes)
'''

print(f"\nEl tiempo total de carrera del equipo ganador fue: {minutos_totales_entero:.0f} minutos {segundos_restantes_entero:.0f}"
      f" segundos {centesimas_restantes:.0f} centesimas.")

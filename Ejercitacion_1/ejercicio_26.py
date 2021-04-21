'''
26- Tiempos de triatlón

Un triatlón es una competición deportiva en que los participantes realizan tres carreras:
una de natación, una ciclista y una pedestre.
Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos)
logrados en cada etapa por uno de los deportistas participantes.
Con esos datos determinar:
* Tiempo total de la prueba (en formato hh:mm:ss)
* Tiempo máximo y mínimo (en segundos)
* Tiempo promedio de las pruebas (en segundos, redondeado a 2 decimales)
Consejo: convertir a segundos los horarios ingresados, para facilitar las operaciones.
'''

natacion = input("\ningresar el tiempo de la carrera de natacion del participante "
                 "(en minutos : segundos):")
ciclismo = input("\ningresar el tiempo de la carrera de ciclismo del participante "
                 "(en minutos : segundos):")
pedestre = input("\nngresar el tiempo de la carrera de pedestre del participante "
                 "(en minutos : segundos): ")

minutos_natacion = natacion[0] + natacion[1]
segundos_natacion = natacion[3] + natacion[4]
minutos_ciclismo = ciclismo[0] + ciclismo[1]
segundos_ciclismo = ciclismo[3] + ciclismo[4]
minutos_pedestre = pedestre[0] + pedestre[1]
segundos_pedestre = pedestre[3] + pedestre[4]

minutos_natacion_int = int(minutos_natacion)
segundos_natacion_int = int(segundos_natacion)
minutos_ciclismo_int = int(minutos_ciclismo)
segundos_ciclismo_int = int(segundos_ciclismo)
minutos_pedestre_int = int(minutos_pedestre)
segundos_pedestre_int = int(segundos_pedestre)

minutos_a_segundos_natacion = minutos_natacion_int * 60
minutos_a_segundos_ciclismo = minutos_ciclismo_int * 60
minutos_a_segundos_pedestre = minutos_pedestre_int * 60

suma_total_segundos_natacion = minutos_a_segundos_natacion + segundos_natacion_int
suma_total_segundos_ciclismo = minutos_a_segundos_ciclismo + segundos_ciclismo_int
suma_total_segundos_pedestre = minutos_a_segundos_pedestre + segundos_pedestre_int

suma_total_segundos_todas_las_pruebas = suma_total_segundos_ciclismo + suma_total_segundos_natacion + suma_total_segundos_pedestre

horas_totales_3pruebas = ((suma_total_segundos_todas_las_pruebas / 60)/ 60)
horas_totales_3pruebas_entero = (horas_totales_3pruebas) - (horas_totales_3pruebas%1)
minutos_totales_3pruebas = ((horas_totales_3pruebas%1) * 60)
minutos_totales_3pruebas_entero = (minutos_totales_3pruebas) - (minutos_totales_3pruebas%1)
segundos_totales_3pruebas = ((minutos_totales_3pruebas%1) * 60)

print(f"Tiempo total de las pruebas es igual a: {horas_totales_3pruebas_entero:.0f}hs {minutos_totales_3pruebas_entero:.0f}min {segundos_totales_3pruebas:.0f}seg")

tiempo_maximo = max(suma_total_segundos_natacion, suma_total_segundos_ciclismo, suma_total_segundos_pedestre)
tiempo_minimo = min(suma_total_segundos_natacion, suma_total_segundos_ciclismo, suma_total_segundos_pedestre)

print(f"Tiempo maximo de las pruebas en segundos: {tiempo_maximo}seg")
print(f"Tiempo minimo de las pruebas en segundos: {tiempo_minimo}seg")

tiempo_promedio_pruebas = suma_total_segundos_todas_las_pruebas / 3

print(f"Tiempo promedio de las pruebas en segundos: {tiempo_promedio_pruebas:.2f}seg")

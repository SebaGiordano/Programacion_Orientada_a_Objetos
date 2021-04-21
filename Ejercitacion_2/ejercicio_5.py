'''
5. Postulantes a un empleo

Se tienen los datos de tres postulantes a un empleo, a los que se les realizó un test
de capacitación.
Por cada postulante, se tiene entonces la siguiente información:
nombre del postulante, cantidad total de preguntas que se le realizaron y cantidad
de preguntas que contestó correctamente.
Se pide confeccionar un programa que lea los datos de los tres postulantes,
informe el nivel de cada uno según los criterios de aprobación que se indican mas abajo,
e indique finalmente el nombre del postulante que ganó el puesto.
Los criterios de aprobación son los siguientes, en función del porcentaje de respuestas
correctas sobre el total de preguntas realizadas a cada postulante:

•	Nivel Superior: Porcentaje 90 %
•	Nivel Medio: 75 % Porcentaje < 90 %
•	Nivel Regular: 50 % Porcentaje < 75 %
•	Fuera de Nivel: Porcentaje < 50 %
'''

print(">>>>> VACANTE DE EMPLEO <<<<<\n"
      "\n    Test de Capacitacion\n")

mayor = None

for i in range(0,3):
    nombre = input(f"Nombre del postulante {i+1}: ")
    cantidad_preguntas = int(input(f"Cantidad de preguntas hechas: "))
    respuestas_correctas = int(input(f"Cantidad de respuestas correctas: "))
    porcentaje_nivel_de_empleo = ((respuestas_correctas * 100) / cantidad_preguntas)
    print(f"El nivel de {nombre} en base al test realizado, es: {porcentaje_nivel_de_empleo:.0f}%")

    if porcentaje_nivel_de_empleo >= 90:
        print(f"El/La postulante {nombre} ha acertado {respuestas_correctas} respuestas correctas "
              f"de {cantidad_preguntas}, por lo que su nivel es Superior")
    elif porcentaje_nivel_de_empleo < 90 and porcentaje_nivel_de_empleo >= 75:
        print(f"El/La postulante {nombre} ha acertado {respuestas_correctas} respuestas correctas "
              f"de {cantidad_preguntas}, por lo que su nivel es Medio")
    elif porcentaje_nivel_de_empleo < 75 and porcentaje_nivel_de_empleo >= 50:
        print(f"El/La postulante {nombre} ha acertado {respuestas_correctas} respuestas correctas "
              f"de {cantidad_preguntas}, por lo que su nivel es Regular")
    elif porcentaje_nivel_de_empleo < 50:
        print(f"El/La postulante {nombre} ha acertado {respuestas_correctas} respuestas correctas "
              f"de {cantidad_preguntas}, por lo que está fuera de nivel")

    if mayor is None or porcentaje_nivel_de_empleo > mayor:
        mayor = porcentaje_nivel_de_empleo

print(f"\nEl postulante ganador de la vacante de empleo, es: {nombre}, "
      f"con un nivel de {mayor:.0f}%")

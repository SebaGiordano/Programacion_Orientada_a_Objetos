'''
3. Cálculo de Regularidad

La facultad pide un simple programa que pida las tres notas de un alumno en cualquier materia
y mostrar si el alumno esta libre, regular o promocionado.
Las tres notas son los dos parciales mas la nota de prácticos y las condiciones
de regularidad están descriptas a continuación:

•	El promedio menor a 4 el alumno esta libre
•	El promedio comprendido entre 4 y 8 el alumno esta regular
•	El promedio mayor a 8 el alumno está promocionado.
'''

materia = input("Asignatura: ")

print("\nDebera ingresar las tres notas correspondientes a los dos parciales "
      "mas la nota de prácticos.\n")

acum = 0

for i in range(0,3):
    num = input(f"Nota {i+1}: ")
    acum = acum + int(num)
    promedio = acum / 3

print()

if promedio < 4:
    print(f"Condicion en {materia}: Libre")
elif promedio >= 4 == 8:
    print(f"Condicion en {materia}: Regular")
elif promedio > 8:
    print(f"Condicion en {materia}: Promocionado")

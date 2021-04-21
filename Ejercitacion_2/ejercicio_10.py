'''
10. Mantenimiento informático

El Área de Mantenimiento de un laboratorio informático nos ha solicitado el desarrollo
de un programa que facilite la gestión de las tareas realizadas en el día.
El usuario debe ingresar de tres equipos informáticos (PC) los siguientes datos:
número de identificación de la PC, tiempo de reparación (expresado en minutos)
y la causa de mantenimiento (1- Problema de Hardware, 2- Problema de Software)

Los requerimientos funcionales son:

• ¿Cuál es el tiempo total de las tareas de mantenimiento?
• ¿Cuál es la PC (Número de identificación) que tuvo mayor tiempo en tareas de mantenimiento?
• Tiempo promedio de tareas de mantenimiento.
• Informar con un mensaje si todas las PC a las que se les ha realizado mantenimiento tuvieron
problemas de hardware.
'''

print(">>>>>>>>>>>>>>> M E N U <<<<<<<<<<<<<<<<<"
      "Tareas realizadas en el día"
      "Debe ingresar de tres equipos informáticos, los siguientes datos:"
      "Número de identificación"
      "Tiempo de reparación (expresado en minutos)"
      "Causa de mantenimiento, para ello: "
      "PRESIONE '1' si la causa es Problema de Hardware"
      "PRESIONE '2' si la causa es Problema de Software\n")

cont1 = 0
cont2 = 0
acum = 0
lista = []

for i in range(3):
    print(f"PC {i+1}")
    id = int(input("Número de identificación: "))
    time = int(input("Tiempo de reparación (expresado en minutos): "))
    acum = acum + time
    problem = int(input("Causa de mantenimiento: "))
    lista.extend([time, id])
    if problem == 1:
        cont1 = cont1 + 1
    elif problem == 2:
        cont2 = cont2 + 1

promedio_de_mantenimiento = acum / 3

print(f"\nEl tiempo total de las tareas de mantenimiento es: {acum} minutos\n")

if lista[0] > lista[2] and lista[0] > lista[4]:
    print(f"La PC:'{lista[1]}' tuvo el mayor tiempo en tareas de mantenimiento, cuyo "
          f"tiempo fue:'{lista[0]}' minutos\n")
elif lista[2] > lista[0] and lista[2] > lista[4]:
    print(f"La PC:'{lista[3]}' tuvo el mayor tiempo en tareas de mantenimiento, cuyo "
          f"tiempo fue:'{lista[2]}' minutos\n")
elif lista[4] > lista[0] and lista[4] > lista[2]:
    print(f"La PC:'{lista[5]}' tuvo el mayor tiempo en tareas de mantenimiento, cuyo "
          f"tiempo fue:'{lista[4]}' minutos\n")

print(f"Tiempo promedio de tareas de mantenimiento: {promedio_de_mantenimiento:.0f} minutos\n")

if cont1 == 3:
    print("Todas las PC a las que se les ha realizado mantenimiento tuvieron problemas de Hardware")
else:
    print("No todas las PC a las que se les ha realizado mantenimiento tuvieron problemas de Hardware")

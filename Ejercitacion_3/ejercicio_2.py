'''
2. Ciclistas

La final de una carrera de ciclistas tiene n competidores.
Se pide cargar los datos de cada competidor (nombre y tiempo de carrera,
validando que el tiempo no sea negativo).
La carga finaliza ingresando un cero como nombre del ciclista. Se pide:

•	Determinar y mostrar el nombre del ganador de la carrera.
•	Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del
ganador es menor al tiempo record, mostrar un mensaje.
•	Calcular y mostrar el tiempo promedio entre todos los ciclistas.
'''

print("\nIngrese '1' para cargar el nombre y el tiempo de carrera del ciclista\n"
      "Ingrese '0' en el nombre del ciclista para finalizar la carga y proceder a cargar "
      "el tiempo record registrado para la carrera\n"
      "Ingrese '2' para salir del sistema\n")

opcion = int(input("Ingrese una opcion: "))

lista_tiempos = []
lista_tiempos_y_ciclistas = []
cont = 0
acum = 0

while opcion != 2:
    if opcion == 1:
        nombre = input(f"\nNombre del ciclista: ")
        if nombre == '0':

            tiempo_record_registrado = float(input("\nTiempo record registrado para la carrera: "))

            menor_tiempo_carrera = min(lista_tiempos)
            ganador_carrera = min(lista_tiempos_y_ciclistas)
            tiempo_promedio = acum / cont

            print(f"\nEl ganador de la carrera con un tiempo de: {ganador_carrera}")

            if float(menor_tiempo_carrera) < tiempo_record_registrado:
                print(f"El ganador ha superado el record registrado de {tiempo_record_registrado} minutos"
                      f" registrando un nuevo record de {menor_tiempo_carrera}")
            else:
                print("El tiempo carrera del ganador no ha de alcanzar el record registrado para la misma")

            print(f"El tiempo promedio entre todos los ciclistas es: {tiempo_promedio} minutos")
            break
        else:
            cont = cont + 1
            tiempo_de_carrera = float(input("Tiempo de carrera: "))
            if tiempo_de_carrera < 0:
                print("\nERROR!, no puede ingresar un numero negativo. Vuelve a intentarlo\n")
                tiempo_de_carrera = float(input("Tiempo de carrera: "))
            acum = acum + tiempo_de_carrera
            lista_tiempos.append(str(tiempo_de_carrera))
            lista_tiempos_y_ciclistas.append(str(tiempo_de_carrera) + ' min' + ' fue, el ' + 'Participante: ' + nombre)
    else:
        print("Opcion incorrecta. Vuelve a intentarlo!!!")
        opcion = int(input("\nIngrese una opcion: "))

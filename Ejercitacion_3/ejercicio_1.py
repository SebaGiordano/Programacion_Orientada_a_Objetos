'''
1. Desarrollar un programa que permita procesar funciones de un complejo de cines.
Por cada función se conoce: cantidad de espectadores y descuento (S/N).
La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).

El programa deberá:

• Calcular la recaudación total del complejo, considerando que el valor de la entrada
es de $50 en los días con descuento y $75 en los días sin descuento.
• Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre
el total de funciones.
'''


def presentacion():
    print("\n      >>>>>> COMPLEJO DE CINES <<<<<<\n"
          "\nDIAS CON DESCUENTO          DIAS SIN DESCUENTO\n"
          "Lunes $50                   Viernes $75\n"
          "Martes $50                  Sabado $75\n"
          "Miercoles $50               Domingo $75\n"
          "Jueves $50")


presentacion()


def menu_principal():
    print("\n>>>>>>>>>> MENU DE OPCIONES <<<<<<<<<<<\n"
          "Ingrese '1' para cargar funciones del dia Lunes\n"
          "Ingrese '2' para cargar funciones del dia Martes\n"
          "Ingrese '3' para cargar funciones del dia Miercoles\n"
          "Ingrese '4' para cargar funciones del dia Jueves\n"
          "Ingrese '5' para cargar funciones del dia Viernes\n"
          "Ingrese '6' para cargar funciones del dia Sabado\n"
          "Ingrese '7' para cargar funciones del dia Domingo\n"
          "Ingrese '8' para visualizar los resultados del proceso de funciones\n"
          "Ingrese '9' para salir del sistema\n")

    return int(input("Ingrese una opcion: "))


def menu():
    op = menu_principal()
    acum_descuento = 0
    acum_sin_descuento = 0
    cont_descuento = 0
    cont_sin_descuento = 0

    while op != 9:
        if op == 1:
            funciones = int(input("\nCantidad de funciones del dia Lunes: "))
            for i in range(funciones):
                print(f"\nFuncion {i + 1}:")
                cant_espectadores = int(input("Cantidad de espectadores: "))
                if cant_espectadores == 0:
                    break
                descuento = int(input("Valor de la entrada con descuento: "))
                recaudacion = cant_espectadores * descuento
                cont_descuento += 1
                acum_descuento = acum_descuento + recaudacion
            op = menu_principal()
        elif op == 2:
            funciones = int(input("\nCantidad de funciones del dia Martes: "))
            for i in range(funciones):
                print(f"\nFuncion {i + 1}:")
                cant_espectadores = int(input("Cantidad de espectadores: "))
                if cant_espectadores == 0:
                    break
                descuento = int(input("Valor de la entrada con descuento: "))
                recaudacion = cant_espectadores * descuento
                cont_descuento += 1
                acum_descuento = acum_descuento + recaudacion
            op = menu_principal()
        elif op == 3:
            funciones = int(input("\nCantidad de funciones del dia Miercoles: "))
            for i in range(funciones):
                print(f"\nFuncion {i + 1}:")
                cant_espectadores = int(input("Cantidad de espectadores: "))
                if cant_espectadores == 0:
                    break
                descuento = int(input("Valor de la entrada con descuento: "))
                recaudacion = cant_espectadores * descuento
                cont_descuento += 1
                acum_descuento = acum_descuento + recaudacion
            op = menu_principal()
        elif op == 4:
            funciones = int(input("\nCantidad de funciones del dia Jueves: "))
            for i in range(funciones):
                print(f"\nFuncion {i + 1}:")
                cant_espectadores = int(input("Cantidad de espectadores: "))
                if cant_espectadores == 0:
                    break
                descuento = int(input("Valor de la entrada con descuento: "))
                recaudacion = cant_espectadores * descuento
                cont_descuento += 1
                acum_descuento = acum_descuento + recaudacion
            op = menu_principal()
        elif op == 5:
            funciones = int(input("\nCantidad de funciones del dia Viernes: "))
            for i in range(funciones):
                print(f"\nFuncion {i + 1}:")
                cant_espectadores = int(input("Cantidad de espectadores: "))
                if cant_espectadores == 0:
                    break
                descuento = int(input("Valor de la entrada sin descuento: "))
                recaudacion = cant_espectadores * descuento
                cont_sin_descuento += 1
                acum_sin_descuento = acum_sin_descuento + recaudacion
            op = menu_principal()
        elif op == 6:
            funciones = int(input("\nCantidad de funciones del dia Sabado: "))
            for i in range(funciones):
                print(f"\nFuncion {i + 1}:")
                cant_espectadores = int(input("Cantidad de espectadores: "))
                if cant_espectadores == 0:
                    break
                descuento = int(input("Valor de la entrada sin descuento: "))
                recaudacion = cant_espectadores * descuento
                cont_sin_descuento += 1
                acum_sin_descuento = acum_sin_descuento + recaudacion
            op = menu_principal()
        elif op == 7:
            funciones = int(input("\nCantidad de funciones del dia Domingo: "))
            for i in range(funciones):
                print(f"\nFuncion {i + 1}:")
                cant_espectadores = int(input("Cantidad de espectadores: "))
                if cant_espectadores == 0:
                    break
                descuento = int(input("Valor de la entrada sin descuento: "))
                recaudacion = cant_espectadores * descuento
                cont_sin_descuento += 1
                acum_sin_descuento = acum_sin_descuento + recaudacion
            op = menu_principal()
        elif op == 8:
            recaudacion_total = acum_descuento + acum_sin_descuento
            funciones_totales = cont_descuento + cont_sin_descuento
            porcentaje_de_funciones_con_descuento = (cont_descuento * 100) / funciones_totales
            porcentaje_de_funciones_sin_descuento = (cont_sin_descuento * 100) / funciones_totales

            print(f"\nLa recaudacion total del complejo de cines fue de: ${recaudacion_total}")
            print(f"\nSe efectuaron {cont_descuento} funciones con descuento, las cuales"
                  f" represental el {porcentaje_de_funciones_con_descuento:.0f}% de las "
                  f"funciones totales")
            break
        else:
            print("Opcion incorrecta!!! Vuelve a intentarlo.")
            op = menu_principal()


menu()

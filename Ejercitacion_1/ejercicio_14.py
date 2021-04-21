'''
14- Votación en el Congreso

En el Congreso se vota la sanción de una ley muy importante. Desarrollar un programa
que permita ingresar la cantidad de votos a favor y en contra, e informe el
porcentaje obtenido en cada caso.
'''


def opciones_del_menu():
    print("\n>>> S A N C I O N  D E  L E Y <<<")
    print("\n1 voto positivo"
          "\n2 voto negativo")

    return int(input("\nPrecione '0' para salir del sistema"
                     "\nPresione '1' si usted esta a favor"
                     "\nPresione '2' si usted esta encontra"
                     "\nPrecione '3' para saber la cantidad de votos positivos"
                     "\nPrecione '4' para saber la cantidad de votos negativos"
                     "\nPrecione '5' si desea saber el total de votos"
                     "\nPrecione '6' si desea saber el porcentaje de votos a favor"
                     "\nPrecione '7' si desea saber el porcentaje de votos en contra\n"
                     "\n>>> Opcion: "))


def menu():
    opcion = opciones_del_menu()
    cont_positivo = 0
    cont_negativo = 0
    cont_total = 0

    while opcion != 0:
        if opcion == 1:
            print("\nVoto Positivo")
            cont_positivo = (cont_positivo + 1)
            cont_total = cont_total + 1
        elif opcion == 2:
            print("\nVoto Negativo")
            cont_negativo = (cont_negativo + 1)
            cont_total = cont_total + 1
        elif opcion == 3:
            print(f"\nLa cantidad de votos positivos es: {cont_positivo}")
        elif opcion == 4:
            print(f"\nLa cantidad de votos negativos es: {cont_negativo}")
        elif opcion == 5:
            print(f"El total de votos fue: {cont_total}")
        elif opcion == 6:
            print(f"El porcentaje de votos positivos fue: %{((cont_positivo*100)/cont_total)}")
        elif opcion == 7:
            print(f"El porcentaje de votos negativos fue: %{((cont_negativo*100)/cont_total)}")
        else:
            print("ERROR! Opcion incorrecta. Vuelva a intentarlo!!!")

        opcion = opciones_del_menu()


menu()

from Analista_de_Sistemas_2do.POO.Ejercitacion_8.clase_vehiculo import Vehiculo
from Analista_de_Sistemas_2do.POO.Ejercitacion_8.clase_auto import Auto
from Analista_de_Sistemas_2do.POO.Ejercitacion_8.clase_moto import Moto
from Analista_de_Sistemas_2do.POO.Ejercitacion_8.clase_camion import Camion


def opciones_del_menu_1():
    print("\n##########################################################\n"
          "## BIENVENIDO AL PRIMER MENU DE OPCIONES DE 'Vehiculos' ##"
          "\n##########################################################\n"
          "Presione [1] para crear un vehiculo\n"
          "Presione [2] para mostrar datos de los vehiculos\n"
          "Presione [3] para acceder al tercer menu para consultar el mantenimiento "
          "del vehiculo seleccionado y realizar posibles modificaciones\n"
          "Presione [0] para salir del sistema\n")


def opciones_del_menu_2():
    print("\n###########################################################\n"
          "## BIENVENIDO AL SEGUNDO MENU DE OPCIONES DE 'Vehiculos' ##"
          "\n###########################################################\n"
          "Presione [a] para crear un objeto auto\n"
          "Presione [b] para crear un objeto moto\n"
          "Presione [c] para crear un objeto camion\n"
          "Presione [d] para salir del sistema y volver al menu anterior\n")


def opciones_del_menu_3():
    print("\n##########################################################\n"
          "## BIENVENIDO AL TERCER MENU DE OPCIONES DE 'Vehiculos' ##"
          "\n##########################################################\n"
          "Presione [1] para consultar acerca del mantenimiento del vehiculo (auto-moto-camion)\n"
          "Presione [2] para modificar la marca (auto-moto-camion)\n"
          "Presione [3] para modificar la cantidad de ruedas (auto-moto-camion)\n"
          "Presione [4] para modificar el tipo de combustible (auto-moto-camion)\n"
          "Presione [5] para modificar la velocidad maxima (auto-moto-camion)\n"
          "Presione [6] para modificar el tipo de vehiculo (camion = Semi o Acoplado, "
          "moto = Todoterreno o Ciudad)\n"
          "Presione [7] para modificar los espejos trovisores (moto)\n"
          "Presione [8] para modificar la cantidad de puertas (auto)\n"
          "Presione [9] para modificar el color (auto)\n"
          "Presione [0] para salir del sistema y volver al menu anterior\n")


def menu():
    vehiculos = []
    opciones_del_menu_1()
    opcion = int(input('Ingrese la opcion deseada: '))

    while opcion != 0:
        if opcion == 1:
            opciones_del_menu_2()
            op = input('Ingrese la opcion deseada: ')

            while op != 'd':
                if op == 'a':
                    marca = input("\nMarca: " or '')
                    cantidad_de_ruedas = int(input("Cantidad de ruedas: "))
                    tipo_de_combustible = input("Tipo de combustible: ")
                    velocidad_maxima = float(input("Velocidad maxima: "))
                    cantidad_de_puertas = float(input("Cantidad de puertas: "))
                    color = input("Color: ")
                    vehiculos.append(Auto(marca, cantidad_de_ruedas, tipo_de_combustible, velocidad_maxima,
                                          cantidad_de_puertas, color))
                    print("\nEl objeto vehiculo fue creado exitosamente!")

                elif op == 'b':
                    marca = input("\nMarca: " or '')
                    cantidad_de_ruedas = int(input("Cantidad de ruedas: "))
                    tipo_de_combustible = input("Tipo de combustible: ")
                    velocidad_maxima = float(input("Velocidad maxima: "))
                    espejo_retrovisor = input("Tiene Espejo Retrovisor? [SI / NO]: ")
                    tipo = input("Tipo ['Todo terreno' / 'Ciudad']: ")
                    vehiculos.append(Moto(marca, cantidad_de_ruedas, tipo_de_combustible, velocidad_maxima,
                                          espejo_retrovisor, tipo))
                    print("\nEl objeto vehiculo fue creado exitosamente!")

                elif op == 'c':
                    marca = input("\nMarca: " or '')
                    cantidad_de_ruedas = int(input("Cantidad de ruedas: "))
                    tipo_de_combustible = input("Tipo de combustible: ")
                    velocidad_maxima = float(input("Velocidad maxima: "))
                    tipo = input("Tipo ['semi' / 'acoplado']: ")
                    vehiculos.append(Camion(marca, cantidad_de_ruedas, tipo_de_combustible,
                                            velocidad_maxima, tipo))
                    print("\nEl objeto vehiculo fue creado exitosamente!")

                else:
                    print("Opcion incorrecta!!!")

                opciones_del_menu_2()
                op = input('Ingrese la opcion deseada: ')

            opciones_del_menu_1()
            opcion = int(input('Ingrese la opcion deseada: '))

            while opcion != 0:

                if opcion == 2:
                    for vehiculo in vehiculos:
                        print(vehiculos.index(vehiculo), '=', vehiculo)

                elif opcion == 3:
                    indice = int(input('Ingrese el indice del vehiculo que desea seleccionar: '))
                    while indice >= len(vehiculos):
                        indice = int(input('Error!! Indice incorrecto. Vuelve a Ingresar el indice del vehiculo: '))

                    opciones_del_menu_3()
                    opp = int(input('Ingrese la opcion deseada: '))

                    while opp != 0:
                        if opp == 1:
                            mantenimiento = vehiculos[indice].realizarMantenimiento()
                            print(f"\nEl mantenimiento del vehiculo debe realizarse a partir de los {mantenimiento:.2f} km")

                        elif opp == 2:
                            vehiculos[indice].marca = input('Actualizar marca: ')

                        elif opp == 3:
                            vehiculos[indice].cantidad_de_ruedas = int(input('Actualizar cantidad de ruedas: '))

                        elif opp == 4:
                            vehiculos[indice].tipo_de_combustible = input('Actualizar tipo de combustible: ')

                        elif opp == 5:
                            vehiculos[indice].velocidad_maxima = int(input('Actualizar velocidad maxima: '))

                        elif opp == 6:
                            vehiculos[indice].tipo = input('Actualizar tipo: ')

                        elif opp == 7:
                            vehiculos[indice].tiene_espejo_retrovisor()

                        elif opp == 8:
                            vehiculos[indice].cantidad_de_puertas = int(input('Actualizar cantidad de puertas: '))

                        elif opp == 9:
                            vehiculos[indice].color = input('Actualizar color: ')

                        else:
                            print("Opcion incorrecta!!!")

                        opciones_del_menu_3()
                        opp = int(input('Ingrese la opcion deseada: '))

                else:
                    print("Opcion incorrecta!!!")

                opciones_del_menu_1()
                opcion = int(input('Ingrese la opcion deseada: '))

            if opcion == 0:
                break

        elif opcion == 2:
            print("Error! No es posible mostrar un vehiculo si antes no fue creado. Vuelve a intentarlo!")

        elif opcion == 3:
            print("Error! No es posible acceder al tercer menu para consultar el mantenimiento "
                  "de un vehiculo y realizar modificaciones si antes no fue creado. "
                  "Vuelve a intentarlo!")

        else:
            print("Opcion incorrecta!!!")

        opciones_del_menu_1()
        opcion = int(input('Ingrese la opcion deseada: '))


menu()

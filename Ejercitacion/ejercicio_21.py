'''
21- Control electoral

Desarrollar un programa de control electoral en un centro vecinal, en el que se
ingresen, para cierto candidato: apellido, nombre y cantidad de votos.
Luego presentar en pantalla un resumen que muestre: iniciales del candidato,
cantidad de votos entre paréntesis, y debajo una línea con tantas “x”
como votos obtenidos (por ejemplo, el candidato obtuvo 4 votos, deberá aparecer
una línea como esta: “xxxx” con cuatro letras “x”)
(Asumimos que en el centro vecinal no hay demasiados electores, de forma que podamos
estar seguros que no habrá miles o millones de votos…
sólo unos pocos para darle sentido al enunciado).
'''


def opciones_del_menu():
    print("\n>>> CONTROL ELECTORAL <<<")

    return int(input("\nPresione '0' para salir del sistema"
                     "\nPresione '1' para ingresar nombre del candidato"
                     "\nPresione '2' para ingresar apellido del candidato"
                     "\nPresione '3' para ingresar la cantidad de votos"
                     "\nPresione '4' para presentar en pantalla un resumen de los candidatos\n"
                     ">>> Opcion: "))


def menu():
    opcion = opciones_del_menu()

    while opcion != 0:
        if opcion == 1:
            a = str(input("\nNombre del Candidato: "))
        elif opcion ==2:
            b = str(input("\nApellido del Candidato: "))
        elif opcion == 3:
            c = int(input("Ingrese la cantidad de votos: "))
        elif opcion == 4:
            inicial_nombre = a[0]
            inicial_apellido = b[0]
            print(f"\n{inicial_nombre}{inicial_apellido} ({c})")
            linea_x = 'x'*c
            print(linea_x)
        else:
            print("ERROR! Opcion incorrecta. Vuelva a intentarlo!!!")

        opcion = opciones_del_menu()


menu()

# OTRA RESOLUCION

nombre_candidato= input(f"Ingrese el nombre del candidato: ")

apellido_candidato= input(f"Ingrese el apellido del candidato: ")

cantidad_votos_candidato= int(input(f"Ingrese la cantidad de votos que recibió el candidato: "))


inicial_nombre= nombre_candidato[0]

inicial_apellido= apellido_candidato[0]

print(f"{inicial_nombre}{inicial_apellido} ({cantidad_votos_candidato})")

cantidad_x= "X"*cantidad_votos_candidato

print(cantidad_x)

'''
1- Secuencia en rango

Desarrollar un programa de Python que permita cargar por teclado un secuencia de números,
uno por uno. Siempre se supone que el usuario cargará un 0(cero) para indicar el final
del proceso de carga.
El cero no debe considerarse un dato a procesar. El programa debe:
Determinar cuantos números se encuentran en el rango definido por 2 números p y q
previamente ingresados (validar que los números que definen el rango son mayores a cero)
Determinar la cantidad de veces que se ingresaron 2 números contiguos pares.
Determinar la cantidad de números que son múltiplos del primer numero de la secuencia
Determinar el porcentaje que representa la cantidad del primer punto sobre el total de números
de la secuencia
'''


def menu_prinsipal():
    print('*' * 69)
    print("** Ingrese [1] para entrar al sistema y comenzar a digitar numeros **")
    print("** Ingrese [0] para finalizar la carga de numeros                  **")
    print("** Ingrese [2] salir del sistema y proceder con los calculos       **")
    print('*' * 69)
    return int(input("\nIngrese una opcion: "))


def porcentaje(rango, total):
    porcentaje_primer_punto = ((len(rango) * 100) / total)
    return porcentaje_primer_punto


def lista_numeros():
    opcion = menu_prinsipal()
    numeros = []

    while opcion == 2:
        print("\nERROR!!! No es posible salir del sistema sin antes haber cargado algun valor numerico."
              " Vuelve a intentarlo!\n")
        opcion = menu_prinsipal()

    while opcion != 2:
        if opcion == 0:
            print("\nERROR!! Aun no ha ingresado ningun valor numero como para finalizar la carga. "
                  "Vuelve a intentarlo!\n")
            opcion = menu_prinsipal()
            while opcion == 2:
                print("\nERROR!!! No es posible salir del sistema sin antes haber cargado algun valor numerico."
                      " Vuelve a intentarlo!\n")
                opcion = menu_prinsipal()
        elif opcion == 1:
            num = int(input("Ingrese un numero: "))
            if num == 0:
                break
            else:
                numeros.append(num)
    return numeros


def main():
    numeros = lista_numeros()

    p = int(input("Ingrese el valor del rango p: "))
    q = int(input("Ingrese el valor del rango q: "))

    if p <= 0:
        p = int(input("ERROR!!! Debe ingresar un valor mayor a '0'. Ingrese nuevamente el rango p: "))
    elif q <= 0:
        q = int(input("ERROR!!! Debe ingresar un valor mayor a '0'. Ingrese nuevamente el rango q: "))

    numeros_entre_rango = []

    for numero in numeros:
        if numero >= p and numero <= q:
            numeros_entre_rango.append(numero)

    contador_num_cont = 0
    num_anterior = 1

    for numero in numeros:
        det_par = int(numero % 2)
        det_par_ant = int(num_anterior % 2)
        if det_par == 0 and det_par_ant == 0:
            contador_num_cont += 1
        num_anterior = int(numero)

    primer_num_secuencia = numeros[0]
    cont_num_multiplos = 0

    for numero in numeros:
        resto = numero % primer_num_secuencia
        if resto == 0 and numero != 0:
            cont_num_multiplos = cont_num_multiplos + 1

    cont = 0

    for numero in numeros:
        if numero != 0:
            cont += 1

    print(f"\nLa cantidad de numeros en el rango p y q son: {len(numeros_entre_rango)}")
    print(f"La cantidad de numeros contiguos pares son: {contador_num_cont}")
    print(f"La cantidad de numeros que son multiplos del primero son: {cont_num_multiplos}")
    print(f"La cantidad de numeros que se encuentran en el rango, representan"
          f" el %{porcentaje(numeros_entre_rango, cont):.2f} del total de numeros de la secuencia.")


main()

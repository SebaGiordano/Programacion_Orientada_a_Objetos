'''
3. Menú de opciones con secuencias
Escribir un programa que le permita al usuario, a través de un menú de opciones,
las siguientes operaciones:

• Generar una serie n de números (n ingresado por teclado y validando que
sea mayor a cero) y mostrar la suma de los cuadrados
• Ingresar un texto finalizado por un punto y determinar la cantidad de palabras
que finalizan con vocales
• Ingresar una serie de números (la carga finaliza con cero) y determinar
si hay mayor cantidad de  valores pares o de impares
• Salir
'''


def menu_principal():
    print("\n====================================================================")
    print("================== M E N U - P R I N S I P A L =====================")
    print("====================================================================\n")
    print("Presione '1' si desea ingresar una serie de numeros y mostrar la suma de los cuadrados\n"
          "Presione '2' si desea ingresar un texto finalizado por un punto\n"
          "Presione '3' si desea ingresar una serie de numeros y saber si hay mayor cantidad de  "
          "valores pares o de impares\n"
          "Presione '4' si desea salir del sistema\n")

    return int(input("Digite una opcion: "))


def menu():
    op = menu_principal()
    suma_cuadrados = 0
    while op != 4:
        if op == 1:
            num = int(input("Cuantos numeros desea ingresar: "))
            for i in range(num):
                num_a_ingresar = int(input(f"Numero {i + 1}: "))
                if num_a_ingresar < 1:
                    print("\nError!, debes ingresar numeros mayores a '0'. Vuelve a intentarlo\n")
                    num_a_ingresar = int(input(f"\nNumero {i + 1}: "))
                cuadrado = (num_a_ingresar ** 2)
                suma_cuadrados = suma_cuadrados + cuadrado
            print(f"\nLa suma de los cuadrados es igual a: {suma_cuadrados}")
            op = menu_principal()
        elif op == 2:
            texto_a_analizar = input(f"Ingrese el texto que desea analizar, finalizado por un punto: ")
            contador_palabras = 0
            caracter_anterior = ''
            vocales = ['a', 'e', 'i', 'o', 'u']
            for caracter in texto_a_analizar:
                if caracter == ' ' or caracter == '.':
                    if caracter_anterior in vocales:
                        contador_palabras = contador_palabras + 1
                caracter_anterior = caracter
            print(f"\nLa cantidad de palabras que terminan con vocales en el texto ingresado "
                  f"es igual a: {contador_palabras}")
            contador_vocales = 0
            for i in vocales:
                for y in texto_a_analizar:
                    if i == y:
                        contador_vocales += 1
            print(f"El numero total de vocales en todo el texto ingresado, es: {contador_vocales}")
            op = menu_principal()
        elif op == 3:
            print("A continuacion debera ingresar una serie de numeros.\n"
                  "Para finalizar la carga de numeros digite '0'\n")
            num_a_ingresar = int(input(f"Numero: "))
            cont_par = 0
            cont_impar = 0
            while num_a_ingresar != 0:
                num_a_ingresar = int(input(f"Numero: "))
                if num_a_ingresar == 0:
                    break
                if num_a_ingresar % 2 == 0:
                    if num_a_ingresar == num_a_ingresar:
                        print("Error! no puede ingresar 2 veces el mismo valor. Vuelve a intentarlo")
                        cont_par += 1
                else:
                    if num_a_ingresar == num_a_ingresar:
                        print("Error! no puede ingresar 2 veces el mismo valor. Vuelve a intentarlo")
                        cont_impar += 1
            if cont_par > cont_impar:
                print(f"\nPares: {cont_par}, Impares: {cont_impar}")
                print("\nHay mayor cantidad de valores pares")
            else:
                print(f"\nPares: {cont_par}, Impares: {cont_impar}")
                print("\nHay mayor cantidad de valores impares")
            op = menu_principal()
        else:
            print("Opcion incorrecta, vuelva a intentarlo")
            op = menu_principal()


menu()

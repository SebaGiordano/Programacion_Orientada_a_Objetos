class Cuenta:
    def __init__(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar_datos(self):
        print(f"Titular de la cuenta: {self.__titular}\n"
              f"Monto: ${self.__cantidad:.2f}")

    def ingresar_dinero(self, valor_nuevo):
        if valor_nuevo > 0:
            valor_total = self.__cantidad + valor_nuevo
            print(f"\nEl monto actualizado luego de haber ingresado ${valor_nuevo:.2f} es: ${valor_total:.2f}")
            self.__cantidad = valor_total
        else:
            print("\nError!! Ha ingresado un saldo negativo. vuelve a intentarlo!")

    def retirar_dinero(self, valor_nuevo):
        if valor_nuevo > 0:
            valor_total = self.__cantidad - valor_nuevo
            if valor_total > 0:
                print(f"\nEl monto actualizado luego de haber extraido ${valor_nuevo:.2f} es: ${valor_total:.2f}")
            else:
                print(f"Luego de haber retirado ${valor_total:.2f} su cuenta esta al rojo vivo, cuyo "
                      f"valor es: ${valor_total:.2f}")
            self.__cantidad = valor_total
        else:
            print("\nError!! Ha ingresado un saldo negativo. vuelve a intentarlo!")


def opciones_del_menu():
    print("\n################################################\n"
          "## BIENVENIDO AL MENU DE OPCIONES DE 'Cuenta' ##"
          "\n################################################\n"
          "Ingrese [1] para cargar una nueva cuenta\n"
          "Ingrese [2] para mostrar los datos de la cuenta\n"
          "Ingrese [3] para ingresar dinero a la cuenta\n"
          "Ingrese [4] para retirar dinero de la cuenta\n"
          "Ingrese [0] para finalizar y acceder a la Cuenta joven\n")

    return int(input("Ingrese una opcion: "))


def menu():
    opcion = opciones_del_menu()

    while opcion != 0:
        if opcion == 1:
            titular = input("\nTitular: ")
            monto = float(input("Monto: "))
            cuenta = Cuenta(titular, monto)
            opcion = opciones_del_menu()
            while opcion != 0:
                if opcion == 2:
                    cuenta.mostrar_datos()
                    opcion = opciones_del_menu()
                if opcion == 3:
                    saldo_a_ingresar = float(input("\nSaldo a ingresar: "))
                    cuenta.ingresar_dinero(saldo_a_ingresar)
                    opcion = opciones_del_menu()
                if opcion == 4:
                    saldo_a_retirar = float(input("\nSaldo a retirar: "))
                    cuenta.retirar_dinero(saldo_a_retirar)
                    opcion = opciones_del_menu()
                if opcion == 0:
                    break
        elif opcion == 2:
            print("Error! No es posible mostrar una cuenta si antes no fue registrada. Vuelve a intentarlo!")
            opcion = opciones_del_menu()
        elif opcion == 3:
            print("Error! No es posible ingresar dinero a una cuenta si antes no fue registrada. Vuelve a intentarlo!")
            opcion = opciones_del_menu()
        elif opcion == 4:
            print("Error! No es posible retirar dinero de una cuenta si antes no fue registrada. Vuelve a intentarlo!")
            opcion = opciones_del_menu()
        else:
            print("Opcion incorrecta!!!")
            opcion = opciones_del_menu()


menu()


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, edad, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def mayor_de_edad(self):
        return self.edad >= 18

    def esTitularValido(self):
        if self.mayor_de_edad() and self.edad < 25:
            return True
        else:
            return False

    def retirar(self, monto):
        if self.esTitularValido():
            super().retirar_dinero(monto)
        else:
            print("No podra retirar dinero!!! No es titular valido")

    def __str__(self):
        super().mostrar_datos()
        return f"Edad: {self.edad}\n" \
               f"Bonificacion: {self.bonificacion}%"


def menu_principal():
    print("\n#####################################################\n"
          "## BIENVENIDO AL MENU DE OPCIONES DE 'CuentaJoven' ##"
          "\n#####################################################\n"
          "Ingrese [1] para cargar una nueva cuenta\n"
          "Ingrese [2] para retirar dinero de la cuenta\n"
          "Ingrese [3] para visualizar los datos del titular\n"
          "Ingrese [0] para finalizar\n")

    return int(input("Ingrese una opcion: "))


def menu_secundario():
    opcion = menu_principal()

    while opcion != 0:
        if opcion == 1:
            titular = input("Ingrese su nombre: ")
            cantidad = float(input("Ingrese el monto de su cuenta: "))
            edad = int(input("Ingrese su edad: "))
            new_cuenta = CuentaJoven(titular, cantidad, edad)
            opcion = menu_principal()
            while opcion != 0:
                if opcion == 2:
                    if new_cuenta.esTitularValido():
                        monto_a_retirar = float(input("\nMonto a retirar: "))
                        new_cuenta.retirar(monto_a_retirar)
                    else:
                        print("No podra retirar dinero de la cuenta!!! No es titular valido")
                    opcion = menu_principal()
                elif opcion == 3:
                    print(new_cuenta.__str__())
                    opcion = menu_principal()
                elif opcion == 0:
                    break
        elif opcion == 2:
            print("Error! No es posible retirar dinero de la cuenta si antes no fue registrada. Vuelve a intentarlo!")
            opcion = menu_principal()
        elif opcion == 3:
            print("Error! No es posible mostrar los datos de la cuenta si antes no fue registrada. Vuelve a intentarlo!")
            opcion = menu_principal()
        else:
            print("Opcion incorrecta!!!")
            opcion = menu_principal()


menu_secundario()

class Persona:
    def __init__(self, nombre, edad, DNI):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_DNI(self):
        return self.__DNI

    def set_DNI(self, DNI):
        self.__DNI = DNI

    def mostrar_persona(self):
        print(f"Hola, mi nombre es {self.__nombre}. Tengo {self.__edad} años. Mi DNI es {self.__DNI}")

    def mayor_de_edad(self):
        if self.__edad > 18:
            print(f"Mayor de edad: {True}")
        else:
            print(f"Menor de edad: {False}")


def menu_opciones():
    print("\nIngrese [1] para ingresar los datos de una persona\n"
          "Ingrese [2] para mostrar los datos en pantalla\n"
          "Ingrese [3] para chequear si es mayor de edad\n"
          "Ingrese [0] para salir del sistema\n")

    return int(input("Ingrese una opcion: "))


def menu():
    op = menu_opciones()
    while op != 0:
        if op == 1:
            nombre = input("Ingrese su nombre: ")
            edad = int(input("Ingrese su edad: "))
            dni = int(input("Ingrese su DNI: "))
            persona = Persona(nombre, edad, dni)
            op = menu_opciones()
            while op != 0:
                if op == 2:
                    persona.mostrar_persona()
                    op = menu_opciones()
                elif op == 3:
                    persona.mayor_de_edad()
                    op = menu_opciones()
        elif op == 2:
            print("No sera posible mostrar datos de una persona si antes no se registro")
            op = menu_opciones()
        elif op == 3:
            print("No sera posible verificar si la persona es mayor de edad si antes "
                  "no se registro")
            op = menu_opciones()
        else:
            print("Opcion incorrecta!!!")
            op = menu_opciones()


menu()

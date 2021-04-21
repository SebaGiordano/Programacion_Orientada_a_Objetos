'''
6. Jornal de un Operario

Se necesita desarrollar un programa para el área de recursos humanos de una empresa
que permita informar el jornal de un determinado operario.
Usted deberá cargar por teclado el código de turno que el operario trabajó ese día
(1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.
La política de trabajo en la empresa es que los operarios de la misma pueden
trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno
el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.
'''

print(">>> JORNAL DE UN OPERARIO <<<")
print("\nTURNERO DE TRABAJO\n"
      "'1' Turno Diurno\n"
      "'2' Turno Nocturno\n")

turno = int(input("Digite el codigo del turno trabajado: "))
cant_horas = float(input("Digite la cantidad de horas trabajadas: "))

if turno == 1:
    jornal = cant_horas * 35.50
elif turno ==2:
    jornal = cant_horas * 40.60

print(f"\nEl valor jornal que recibira el trabajador, es: ${jornal}")

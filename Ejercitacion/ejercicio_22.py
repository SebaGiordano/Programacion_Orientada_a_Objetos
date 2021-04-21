'''
22- Cálculo de sueldo

Se conoce el monto del salario actual de un empleado, el nombre del empleado y
el área funcional al cual pertenece. Se pide calcular el nuevo salario del
empleado sabiendo que obtuvo un incremento del 8 % sobre su salario actual y
un descuento de 2,5 % por servicios, informando los resultados con el formato que
se especifica a continuación:
'''

nombre = str(input("Ingrese el nombre de un empleado: "))
salario = float(input(f"Ingrese el salario de {nombre}: "))
area_funcional = str(input(f"Ingrese el area funcional de {nombre}: "))
#INCREMENTO DEL 8%
#DESCUENTO DEL 2,5% POR SERVICIOS
nuevo_salario = ((salario+(salario*0.08))-salario*0.025)
print(f"\nEmpleado: {nombre}\n"
      f"Area funcional: {area_funcional}\n"
      f"Salario actual: ${salario}\n"
      f"Nuevo salario: ${nuevo_salario}")

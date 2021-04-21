'''
18- Fecha como cadena

Desarrollar un programa que cargue por teclado una cadena de caracteres que
se supone representa una fecha en formato “dd/mm/aaaa”, y muestre por separado
el día, el mes y el año. Ejemplo:
si la cadena ingresada es “16/03/2015” el programa debe mostrar:
“Día: 16 - Mes: 03 - Año: 2016”.
'''

fecha_ingresada= str(input(f"Ingrese la fecha en formato dd/mm/aaaa: "))

day = fecha_ingresada[0] + fecha_ingresada[1]

month = fecha_ingresada[3] + fecha_ingresada[4]

year = fecha_ingresada[6] + fecha_ingresada[7] + fecha_ingresada[8] + fecha_ingresada[9]

print(f"Día: {day}; Mes: {month}; Año:{year} ")

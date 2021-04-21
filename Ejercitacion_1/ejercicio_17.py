'''
17- Plazo fijo
Desarrollar un programa que cargue por teclado la cantidad de dinero depositada
en plazo fijo por un cliente de un banco y calcular el saldo que tendrá esa
cuenta al vencer el plazo fijo, sabiendo que el interés pactado era de 2.3 %
y que el banco cobra una tasa fija de gastos por servicios
financieros igual $20 por cuenta.
'''

monto = int(input("> Ingrese el monto depositado a plazo fijo: "))
monto_bruto = monto+(monto*0.023)
monto_total = monto_bruto-20
print(f"\nEl saldo que tendra la cuenta al vencer dicho plazo fijo, es: ${monto_total}")

'''
9- Descuento en medicinas

Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
(cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos
tienen un descuento del 35 %.
Mostrar el precio actual, el monto del descuento y el monto final a pagar.
'''

valor_medicamento = int(input("Ingrese el valor del medicamento: "))
descuento = valor_medicamento*0.35
monto_final = valor_medicamento-descuento
print(f"\nEl valor actual del medicamento es: {valor_medicamento}")
print(f"El monto del descuento es: {descuento}")
print(f"El monto final a pagar es: {monto_final}")

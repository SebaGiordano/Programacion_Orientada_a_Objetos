'''
7- Precio del boleto

Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia.
Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre),
más un valor extra calculado en base a la cantidad de kilómetros a recorrer:
Por cada kilómetro a recorrer se cobra $0,30 de adicional.
'''

monto_base_x_km = 30
monto_adicional_x_km = 0.30

cantidad_de_km = int(input("Cuantos km en omnibus de media distancia desea recorrer? "))
print(f"\nEl precio del boleto es: ${monto_base_x_km+(monto_adicional_x_km*cantidad_de_km)}")

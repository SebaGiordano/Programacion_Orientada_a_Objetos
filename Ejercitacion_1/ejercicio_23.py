'''
23- Cálculo presupuestario

En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología.
El presupuesto anual del hospital se reparte de la siguiente manera:
Urgencias 50%, Pediatría 35% y Traumatología 15%
Cargar por teclado el monto del presupuesto total del hospital, y calcular y
mostrar el monto que recibirá cada área.
'''

presupuesto_total_hospital=int(input(f"Ingrese el presupuesto total del hospital: "))

urgencias= (presupuesto_total_hospital*50)/100

pediatria= (presupuesto_total_hospital*35)/100

traumatologia= (presupuesto_total_hospital*15)/100

print(f"El área de Urgencias recibe ${urgencias} del presupuesto anual del hospital")
print(f"El área de Pediatría recibe ${pediatria} del presupuesto anual del hospital")
print(f"El área de Traumatología recibe ${traumatologia} del presupuesto anual del hospital")
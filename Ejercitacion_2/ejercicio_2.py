'''
2. Impuesto Automotor

Crear un programa que permita calcular los impuestos que debe pagar un auto, conociendo su
modelo (año de fabricación) y tipo (P: Particular / T: Taxi / R: Remis).
Para calcular los impuestos, tener en cuenta que:

• Los autos particulares de menos de 10 años de antigüedad pagan $200, entre 10 y 20 años pagan
$150 y no pagan impuestos los que tienen más de 20 años.
• Los taxis pagan impuestos como auto particular, más $150 por la licencia de taxi.
• Los remises pagan $100 por cada año de antigüedad de su vehículo.
'''

print("Ingrese '1' si es Particular\n"
      "Ingrese '2' si es Taxi\n"
      "Ingrese '3' si es Remis)\n")

oficio = int(input(">> Numero de oficio: "))
vehiculo = input(">> Marca del vehiculo: ")
modelo = int(input(">> Años de antiguedad del vehiculo: "))

if oficio == 1:
    if modelo < 10:
        impuesto_a_pagar = (modelo * 200)
        print(f"\nEl valor del impuesto a pagar es: ${impuesto_a_pagar}")
    elif modelo >= 10 < 20:
        impuesto_a_pagar = (modelo * 150)
        print(f"\nEl valor del impuesto a pagar es: ${impuesto_a_pagar}")
    else:
        print("\nPor su antiguedad no paga impuestos su vehiculo")
elif oficio == 2:
    if modelo < 10:
        impuesto_a_pagar = (modelo * 350)
        print(f"\nEl valor del impuesto a pagar es: ${impuesto_a_pagar}")
    elif modelo == 10 and modelo < 20:
        impuesto_a_pagar = (modelo * 300)
        print(f"\nEl valor del impuesto a pagar es: ${impuesto_a_pagar}")
    else:
        total_a_pagar = (modelo * 150)
        print("\nPor su antiguedad no paga impuestos su vehiculo, solo debe abonar"
              "$150 por la licencia de taxi\n"
              f"El total a pagar es: ${total_a_pagar}")
elif oficio == 3:
    print("\nLos remises pagan $100 por cada año de antigüedad de su vehículo")
    saldo = modelo * 100
    print(f"\nEl saldo total a pagar acorde a su antiguedad es: ${saldo}")
else:
    print("\nERROR!!! inicial incorrcta")

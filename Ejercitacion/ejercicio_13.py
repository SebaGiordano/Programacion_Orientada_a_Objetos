'''
13- Precio de venta
Conociendo el precio de lista de un artículo, determinar:
Precio de venta al contado (10 % de descuento). Precio de venta con tarjeta (5 % de recargo)
'''

precio_lista = int(input("Digite el precio de lista de un producto: "))
al_contado = (precio_lista-(precio_lista*0.10))
print(f"\n>> Abonando el producto al contado tiene un descuento del 10%, cuyo total seria: {al_contado}")
con_targeta = (precio_lista+(precio_lista*0.05))
print(f">> Si desea abonar con targeta, tendra un recargo del 5%, cuyo total seria: {con_targeta}")


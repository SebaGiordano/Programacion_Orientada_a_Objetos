'''
10- Ecuación de Einstein

La famosa ecuación de Einstein para conversión de una masa m en energía viene
dada por la fórmula: 𝐸 = 𝑚𝑐**2
Donde c es la velocidad de la luz cuyo valor es 𝑐 = 299792.458𝑘𝑚/𝑠𝑒𝑔.
Desarrolle un programa que lea el valor de una masa 𝑚 en kilogramos y
obtenga la cantidad de energía 𝐸 producida en la conversión.
'''

m = int(input("Ingrese el valor de una masa en kilogramos: "))
c = 299792.458
e = (m*c)**2
print(f"\nLa cantidad de energía 𝐸 producida en la conversión, es: {e}")

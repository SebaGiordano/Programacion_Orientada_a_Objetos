'''
4. Punto en el plano

Se pide realizar un programa que ingresando el valor x e y de un punto determine
a que cuadrante pertenece en el sistemas de coordenadas.
'''

x = float(input("\nIngrese el valor de 'x': "))
y = float(input("Ingrese el valor de 'y': "))

print()

if x > 0 and y > 0:
    print(f"El punto correspondiente al valor '{x:.0f}' en 'x' y '{y:.0f}' en 'y' pertenecen al primer cuadrante"
          "del eje de coordenadas")
elif x < 0 and y > 0:
    print(f"El punto correspondiente al valor '{x:.0f}' en 'x' y '{y:.0f}' en 'y' pertenecen al segundo cuadrante"
          "del eje de coordenadas")
elif x < 0 and y < 0:
    print(f"El punto correspondiente al valor '{x:.0f}' en 'x' y '{y:.0f}' en 'y' pertenecen al tercer cuadrante"
          "del eje de coordenadas")
elif x > 0 and y < 0:
    print(f"El punto correspondiente al valor '{x:.0f}' en 'x' y '{y:.0f}' en 'y' pertenecen al cuarto cuadrante"
          "del eje de coordenadas")
else:
    print(f"El punto correspondiente al valor '{x:.0f}' en 'x' y '{y:.0f}' en 'y' no pertenecen a ningun"
          f" a ningun cuadrante porque ese punto se encuentra en el origen")

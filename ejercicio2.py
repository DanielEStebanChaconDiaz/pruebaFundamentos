b = float(input("Ingrese la base de su triangulo equilatero:\n"))
a = float(input("Ingrese la altura de su triangulo equilatero:\n"))
area = (b/2)*a
if area > 1000:
    print(f"DATOS NO VALIDOS = {a}, {b}")
else:
    print(f"El area es = {area}")

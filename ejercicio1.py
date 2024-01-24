#Crear un programa que pida 5 voltajes, medir su promedio y visualizar ALTO VOLTAJE si es mayor a 220 caso contrario mostrar VOLTAJE CORRECTO si es menor
v1 = float(input("Ingrese el primer voltaje:\n"))
v2 = float(input("Ingrese el segundo voltaje:\n"))
v3 = float(input("Ingrese el tercer voltaje:\n"))
v4 = float(input("Ingrese el cuarto voltaje:\n"))
v5 = float(input("Ingrese el quinto voltaje:\n"))
prom = (v1+v2+v3+v4+v5)/5
if prom > 220:
    print(f"ALTO VOLTAJE ={prom}")
else:
    print(f"VOLTAJE CORRECTO ={prom}")
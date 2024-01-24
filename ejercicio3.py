# Programa que pida 3 voltajes y analice si es alto, bajo o peligro
v1 = float(input("Ingrese el primer voltaje:\n"))
v2 = float(input("Ingrese el segundo voltaje:\n"))
v3 = float(input("Ingrese el tercer voltaje:\n"))
prom = (v1+v2+v3)/3
if prom > 220:
    print(f"PELIGRO ={prom}")
elif prom <= 220 and prom > 115:
    print(f"ALTO VOLTAJE = {prom}")
else:
    print(f"VOLTAJE CORRECTO ={prom}")
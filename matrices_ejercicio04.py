print("------------------------------------")
print("Matriz3: SUCURSALES DE UNA EMPRESA")
print("------------------------------------")

#inicializar 
MONTO = [] #LISTA VACIA
#ENTRADAS
print("ingrese numero de sucursales y años")
N = int(input("Numero de sucursales: "))
M = int(input("Numero de años: "))
for i in range(M):
	MONTO.append([])
	for j in range(N):
		MONTO[i].append()
print("------------------------------------------------------------")
MAX=0
for i in range(M)
	Suma=0
	for j in range(N):
		Suma=Suma+MONTO[i][j]
	PROM = Suma / N
	print("promedio de ventas del año", i+1, "es", PROM)
	if PROM > MAX:
		MAX = PROM
		ANIO = i+j 
	print(f"año con mayor promedio: {ANIO}")



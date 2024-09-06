print("lectura de n numeros enteros")
print("---------------------------------------------")

i = 1
F=[]

print("ingrese el numero de elementos a ingresar: ")
numElementos=int(input())

while i <= numElementos:
    elemento=(int(input("ingrese elemento: ")))
    F.append(elemento)
    i+=1

print("\nSalida")
print("------------------------------")
print(F)

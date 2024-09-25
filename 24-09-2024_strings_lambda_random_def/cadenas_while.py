#obtener el ultimo elemento de una cadena

fruta = 'banana'
len(fruta)
x = fruta[-1]
print(x)
print("\n")

# recorriendo cadena con un bucle while

fruta = 'banana'
i = 0
while i < len(fruta):
    letra = fruta[i]
    print(letra)
    i += 1

print("\n")
# recorrido con bucle for

fruta = 'banana'
for i in range (len(fruta)):
    letra = fruta[i]
    print(letra)



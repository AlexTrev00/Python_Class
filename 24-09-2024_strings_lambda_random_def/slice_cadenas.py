# slice en cadenas (rebanadas)

s = 'monty python'
print(s[0:5])

print(s[6:12])

fruta= 'banana'
print(fruta[3:])
print(fruta[:3])

fruta = 'banana'
print(fruta[3:3])

# las cadenas no se pueden modificar son inmutables, pero si se puede concatenar una cadena con otra

palabra = """
            ana, ana, bolana, banana, fofana, fi, fai, mo, mana, Ana

"""
contador = 0
for i in palabra:
    if i == 'a' :
        contador += 1
print(i)
        

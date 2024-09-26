''' Cadenas y operador in 
la palabra in es  un operador booleano que toma dos valores y regresa true si se cumplen
'''
R = 'a' in 'banana'
print(R)

# si a se encunetra en banana imprimira 

palabra = 'banana'
if palabra == 'banana':
    print(palabra)


palabra = 'piña'
if palabra > 'banana':
	print("tu palabra " + palabra + " esta antes que banana")
elif palabra < 'banana':
	print("tu palabra " + palabra + " esta despues que banana")
else :
	print("muy bien banana")
# este script ordenara en orden alfabetico las palabras

print("\n")
'''
funcion help podemos obtener una breve documentacion de un metodo
'''
help(str.isalnum)
print("\n")

palabra =  'Monclova, coahuila'
nueva_palabra = palabra.upper()
print(nueva_palabra)

'''
una llamada a un metodo es conocida como una invocacion, en este caso diriamos que estamos
invocando upper en la palabra

por ejemplo, existe un metodo de cadena llamado find que busca la posicion de una cadena
dentro de una cadena dentro de otra: 
'''
palabra = 'banana'
indice = palabra.find('a')
print(indice)


'''
una terea comun es eliminar los espacios en blanco (esapcios, tabs, o nuevas linea)
'''

linea = '   aqui vamos'
print(linea.strip())



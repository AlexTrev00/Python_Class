'''
conjuntos no permiten datos repetidos
los conjuntos se escriben con llaves y no tienen indices, son inmutables pero
se pueden borrar y agregar nuevos elementos
'''

thisset={"apple","banana","cherry"}
print(thisset)


'''
los elementos de los conjuntos son desordenados
'''

thisset = {"apple","banana","cherry","banana"}
print(thisset)

'''
False, True, 0 y 1 el conjunto los tomas como dato tipo boolenaos y los
va a tomar como datos repetidos (si se encuentras los pares juntos como
False y 0 o True y 1 en el mismo conjunto)

'''

thisset = {"apple","banana","cherry","banana",False,0,True,1}
print(thisset)


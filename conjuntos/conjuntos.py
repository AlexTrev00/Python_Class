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

''' conjuntos : interseccion 
conserve SOLO los duplicados
'''

set1 = {"google", "banana", "cherry"}
set2={"google", "microsoft", "banana"}
set3 = set1.intersection(set2)
print(set3)

'''
& para unir dos conjuntos
'''
set1 = {"google", "banana", "cherry"}
set2={"google", "microsoft", "banana"}

set3 = set1 & set2
print(set3)

''' 
el metodo interseccion_update(), tambien mantendra solo los elementos duplicados, pero cambiara el conjunto original en lugar de devolver el nuevo conjunto
'''

set1 = {"google", "banana", "cherry"}
set2={"google", "microsoft", "banana"}
set1.interseccion_update(set2)
print(set1)

'''
conjunto que contienen valores de True y False, 0 y 1 y vera que se considera como duplicado
'''
set1 = {"google", "banana", "cherry","True", "False"}
set2={"google", "microsoft", "banana", 0, 1}
set3= set1.intersection(set2)
prin(set3)

'''
Conjuntos : Diferencia 
el metodo difference() devolvera un nuevo conjunto que considera solo los elementos del primer conjunto que no estan presentes en el otro conjunto

conserva todos lo elementos del set1 que no esten en el set 2
'''
set1 = {"google", "banana", "cherry"}
set2={"google", "microsoft", "banana"}
set3=set1.difference(set2)
print(set3)

'''
se puede utilizar el operador - en lugar del metodo difference() y obtendra el mimso resultado, pero solo se puede usar en conjuntos. 
'''
set1 = {"google", "banana", "cherry"}
set2={"google", "microsoft", "banana"}
set3 = set1 - set2
print(set3)

'''
metodo symmetric_difference() mantendra solo los elementos que NO estan presentes en ambos conjuntos
'''
set1 = {"google", "banana", "cherry"}
set2={"google", "microsoft", "banana"}
set3= set1.symmetric_difference(set2)
print(set3)

'''
puede usar el operador ^ en lugar del metodo symmetric_difference() y se obtendra el mismo resultado, pero solo se puede usar con conjuntos
'''

set1 = {"google", "banana", "cherry"}
set2={"google", "microsoft", "banana"}
set3 = set1 ^ set2
print(set3)

'''
metodo symmetric_difference_update() tambien mantendra todos menos los duplicados, pero cambiara el conjunto original en lugar de devolver un nuevo conjunto
'''
set1 = {"google", "banana", "cherry"}
set2={"google", "microsoft", "banana"}
set1.symmetric_difference_update(set2)
print(set1)

'''
metodo difference_update() conservara los elementos del primer conjunto que no estan en el otro conjunto, pero cambiara el conjunto en lugar de devolver
un nuevo conjunto
'''
set1 = {"google", "banana", "cherry"}
set2={"google", "microsoft", "banana"}
set1.difference_update(set2)
print(set1)



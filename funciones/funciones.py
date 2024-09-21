# funciones
def imprime_lista(lista):
	"""Imprime el parametro lista"""
	if isinstance(lista,list):
		for i in range(0, len(lista),1):
			print(lista[i])

milista=["hola","adios","bye","trece"]
imprime_lista(milista) 

#explicacion: en el bloque if isinstance(lista,list)
# isinstance es una funcion propia de python y veirifca el tipo de un objeto con la ayuda de dos argumentos en este caso 
#(lista,list) el primer argumento (lista) comprueba el tipo de dato u objeto que quieres comprobar y el segundo es el tipo 
# de dato que estas comprobando, en este caso con isinstance(lista,list) comprueba si la lista es realmente un lista. 


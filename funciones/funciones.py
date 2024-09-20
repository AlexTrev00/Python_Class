# funciones
def imprime_lista(lista):
	"""Imprime el parametro lista"""
	if isinstance(lista,list):
		for i in range(0, len(lista),1):
			print(lista[i])

milista=["hola","adios","bye","trece"]
imprime_lista(milista) 


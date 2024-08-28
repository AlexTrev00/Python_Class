name=input("escriba su nombre: ")
gender=input("escriba su genero f para femenino y m masculino: ")
if name < 'm' and gender == "f" or name > 'n' and gender == "m":
	print(f"hola {name} perteneces al grupo A")
else :
	print(f"Hola {name} perteneces al grupo B")

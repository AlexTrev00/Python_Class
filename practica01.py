mujeres=["a","b","c","d","e","f","g","h","i","j","k","l"]
hombres=["ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
user_name=input("escriba su nombre: ")
user_gender=input("esrcriba su genero con M/F : ")
if user_name[0] in mujeres and user_gender == "f" or user_name[0] in hombres and user_gender == "m":
    print(f"hola {user_name} estas en el grupo A")
else:
    print(f"estas {user_name} estas en el grupo B")
    



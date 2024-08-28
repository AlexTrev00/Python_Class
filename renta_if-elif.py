user_renta=float(input("digite su renta: "))
if user_renta < 10000:
	res = (user_renta*0.5)
	print(f"tendra que pagar ${res} euros")
elif (user_renta >= 10000) and (user_renta <= 20000):
	res = (user_renta*0.15)
	print(f"tendra que pagar ${res} euros")
elif (user_renta > 20000) and (user_renta <= 35000):
	res = (user_renta*0.20)
	print = (f"tendra que pagar ${res} euros")
elif (user_renta > 35000) and (user_renta <=60000):
	res= (user_renta*0.30)
	print(f"tendra que pagar ${res} euros")
else:
	res(user_renta*0.45)
	print(f"tendra que pagar ${res} euros")

	

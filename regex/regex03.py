import re

sup_regex=re.compile(r"interroga(ción)?")
mo = sup_regex.search("interrogacion")
print(mo.group())

mo = sup_regex.search("interroga")
print(mo.group())

input()

print('\n---------------------------------------')
# *
ast_regex=re.compile(r"(Ha)*")
mo = ast_regex.search("HaHaHaHaHaHaHaHa")
print(mo.group())

mo = ast_regex.search("") #permite valores nulos
print(mo.group(), "cadena vacia")
input()

print("-----------------------------------------")
# +

plus_regex = re.compile(r"bat(ha)+man")
mo= plus_regex.search("batman")

print(mo)

mo=plus_regex.search("bathahahaman")
print(mo.group())
input()





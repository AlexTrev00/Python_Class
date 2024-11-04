import re 

def regex(tel):
    reg = r'(\d{2}) \d{4}-\d{4}'
    value = re.match(reg, tel)
    return value
# Test the function
num = '81 6456-7895'
print(regex(num))  # True


expresion_telefono_grupo = re.compile(r'\((\d{2})\)(\d{4})-(\{4}')
mo = expresion_telefono_grupo.search('mi numero es (81)8645-9824.')
print("numero encontrado: "+ mo.group())
print("lada", mo.group(1)) #(81)
print("numero", mo.group(2), mo.group(3))


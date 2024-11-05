import re
br_regexp = re.compile(r"batman|robin")
mo = br_regexp.findall("batman, tobin, joker, batman, robin, b a t m a n")
print(mo)
input()

bat_regep = re.compile(r"bat(man|movil|arang)")
mo = bat_regep.search("batman subio a su batimovil olvido su batarang")
print(mo.group())
print(mo.group(1))
mo = bat_regep.findall("batman olvido su batimovil olvido su batarang, batman, ")
print(mo)
input()

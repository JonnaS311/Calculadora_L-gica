import CalculadoraLogica

# p or not q and ( q xor p)          p and w or (q and not w) xor p

cal = CalculadoraLogica.Calculadora()

#print( cal.dos_proposiciones("p or not q and ( q xor not p)"))
print(cal.tres_proposiciones("p and w or ( q and not w )"))
#print(True and False or (True and not False) ^ True)
#print(cal.formula_bien_formulada([True,True,True]))
#print(cal.formula_bien_formulada([True,False,True]))
#print(cal.formula_bien_formulada([False,False,False]))


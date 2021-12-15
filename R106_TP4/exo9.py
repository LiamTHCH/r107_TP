dico = {}
dico['firstname'] = str(input("Prenom :"))
dico['name'] = str(input("Name :"))
dico['promo'] = str(input("Promo :"))
dico['group'] = str(input("Groupe TP : "))
for cle, value in dico.items():
    print(cle,":", value)
tprt111 = {}
tprt111['IUTC426'] = dico
print(tprt111)
import random

def generer(nbr, vmin, vmax):
    l = []
    for i in range(0,nbr):
        l.append(random.randint(vmin, vmax))
    return l
def combieninferieur(ls,seuil):
    return sum(i > seuil for i in ls)
a = int(input("Nombre de chiffre"))
vmax = input("Max")
vmin = input("Min")
s = input("vous voulez préciser le seuil ?")
if s == ("O" or "Oui" or "oui"):
    seuil = int(input("Seuil : "))
elif s == ("N" or "Non" or "non"):
    seuil = 30
else:
    print("erreur")
tab = generer(a, int(vmin), int(vmax))
tab.sort()
print(tab)
total = combieninferieur(tab, seuil)
print("Il y en a %s inférieurs à %s"%(total,seuil))
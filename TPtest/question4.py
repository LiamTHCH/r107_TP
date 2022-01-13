__author__ = "Liam Thomas-Chollier RT111"
def tabl_multi():
    try:
        nb = input("Vous cherchez la table de multiplication de quel nombre ?")
        L = []
        if "." in nb:
            nb = float(nb)
        else:
            nb = int(nb)
        for i in range(0,11):
            L.append(round(i*nb,1))
        return L
    except ValueError:
        print("Erreur, valeur donner n'est ni un entier ni un réel")
        exit(1)
def affich_table(L):
    print("Voici la table de multiplication de ",L[1])
    for i in range(0, len(L)):
        print("%s * %s =  %s" % (i, L[1], L[i]))

affich_table(tabl_multi())
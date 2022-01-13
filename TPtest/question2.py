__author__ = "Liam Thomas-Chollier RT111"
def demande():
    try:
        nb = int(input("Merci de préciser le nombre souhaité :"))
        triangle(nb)
    except ValueError:
        print("Erreur ! Nombre donner n'est pas un entier, recommencer")
        demande()
def triangle(nb):
    ls = [i for i in range(1,nb+1)]
    for i in range(0,nb+1):
        for a in range(i):
            print(ls[a],end="")
            print(" ",end="")
        print("")
    print("")
    for i in range(nb,-1,-1):
        for a in range(i-1,-1,-1):
            print(ls[a], end="")
            print(" ", end="")
        print("")
demande()
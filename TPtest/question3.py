__author__ = "Liam Thomas-Chollier RT111"
def produit_scalair():
    v1 = []
    v2 = []
    calc = 0
    temp = str(input("Merci de saisir les composantes du vecteur V1 :"))
    temp = temp.split(",")
    if len(temp) == 1:
        print("Un des deux vecteurs est composé d'un seul élément ou bien un autre séparateur a été utilisé")
        return -1
    else:
        v1 = temp
    temp = str(input("Merci de saisir les composantes du vecteur V2 :"))
    temp = temp.split(",")
    if len(temp) == 1:
        print("Un des deux vecteurs est composé d'un seul élément ou bien un autre séparateur a été utilisé")
        return -1
    else:
        v2 = temp
    if len(v1) != len(v2):
        print("Les deux vecteurs ne sont pas de même taille")
        return -2
    else:
        for i in range(0, len(v1)):
            calc = calc + (int(v1[i]) * int(v2[i]))
        print("Le produit scalaire de V1 et V2 vaut ",calc)

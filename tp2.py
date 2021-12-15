import datetime
def exo1():
    x = int(input("Entrez x:"))
    y = int(input("Entrez y:"))
    print("")
    swap = [x,y]
    print("Avant permutation:")
    print(" X :",x)
    print(" Y :",y)
    print("")
    x = swap[1]
    y = swap[0]
    print("Apres permutation")
    print("X :",x)
    print("Y :",y)
    print("")

def exo2():
    age = int(input("Donnez votre age :"))
    print(age)
    year = datetime.date.today().year
    anne = year - age
    print("Votre annee de naissance est :",anne)

def exo3():
    a = input("Entrez la premiere  valeur : ")
    b = input("Entrez la deuxieme  valeur : ")
    c = input("Entrez la troisieme valeur : ")

    print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
    print("Permutation: a ==> b, b ==> c, c ==> a")
    """      *******************************************
             * Completez le programme a partir d'ici.
             *******************************************
    """
    swap = [a, b,c]
    a = swap[1]
    b = swap[2]
    c = swap[0]
    """     *******************************************
             * Ne rien modifier apres cette ligne.
             *******************************************
    """

    print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)

def exo4():
    BASE = float(4)
    fromage = float(800.0)
    eau = float(2)
    ail = float(2)
    pain = float(400)
    nb = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
    print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut : ")
    print("- %s gr de fromage "%(fromage*nb/BASE))
    print("- %s dl d'eau " % (eau*nb/BASE))
    print("- %s gousse(s) d'ail" %(ail*nb/BASE))
    print("- %s gr de pain" %(pain*nb/BASE))

def exo5():
    while True:
        signe = str()
        paire = str()
        num = int(input("Nombre :"))
        if num < 0:
            signe = "negatif"
        elif num > 0:
            signe = "postif"
        else:
            signe = "zero"

        if (num % 2) == 0:
            paire = "paire"
        else :
            paire = "impaire"
        if num == 0:
            print("Le nombre est zéro (et il est pair)")
        else:
            print("Le nombre est %s et %s "%(signe,paire))

def exo6():
    x = int(input("Nombre"))
    if ((x<=2) and (x>3)) or ((x<0) and (x>=1)) or ((x>=-10) and (x<=-2)):
        print("x appartient à I")
    else:
        print("x n'appartient pas à I")

def exo7():
    while True:
        try:
            start = int(input("Heure de début: "))
            end = int(input("Heure de fin: "))
        except ValueError:
            print("Entrez un nombre entier!\n")
            continue

        if start in range(25) and end in range(25):
            if start != end:
                if start < end:
                    break
                else:
                    print("Attention ! le début de la location est après la fin ...\n")
            else:
                print("Attention ! l’heure de fin est identique à l’heure de début.\n")
        else:
            print("Les heures doivent être comprises entre 0 et 24 !\n")

    location = []
    for i in range(start, end): location.append(i)

    heuresPleine, heuresCreuses = 0, 0
    for i in location:
        if i in range(7, 17):
            heuresPleine += 1
        else:
            heuresCreuses += 1

    if heuresCreuses != 0: print(" %s heure(s) au tarif de 1€."%(heuresCreuses))
    if heuresPleine != 0: print(" %s heure(s) au tarif de 2€."%(heuresPleine))
    print(f"Le montant total à payer de {heuresCreuses + 2 * heuresPleine}€.")

exo7()


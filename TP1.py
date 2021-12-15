import statistics
import random
import numpy
def exo1(nom,prenom,math,info,anglais,promotion):
    nom = str(nom)
    prenom = str(prenom)
    math = float(math)
    info = float(info)
    anglais = float(anglais)
    promotion = int(promotion)
    moy = statistics.mean([math,info,anglais])
    print("%s %s de la promo %s a comme moyenne %s"%(prenom,nom,promotion,moy))
    print("les variable ot pour type :")
    print("Nom %s ; Prenom %s ; Maths %s ; Info %s ; Anglais %s ; Promotion %s ; Moyenne %s"%(type(nom),type(prenom),type(math),type(info),type(anglais),type(promotion),type(moy)))

def exo2():
    jour = int(20)
    heure = int(14)
    minute = int(20)
    sum = (jour*1440)+(heure*60)+minute
    print(sum)

def exo3():
    jour = int(input("Jours : "))
    heure = int(input("Heure : "))
    minute = int(input("Minutes"))
    if (jour <31) and (heure < 24) and (minute < 60):
        sum = (jour*1440)+(heure*60)+minute
        print(sum)
    else:
        print("Erreur")
def exo4():
    minute = int(input("Nb minute : "))
    jour = (minute//1440)
    print(jour)

def exo5():
    alea = random.randint(0,100)
    print(alea)

def exo6():
    alea = random.randint(0,100)
    print(alea)
    if alea > 50:
        print("face")
    else:
        print("Pile")

def exo7():
    a = numpy.random.choice(numpy.arange(1, 3), p=[2/3,1/3])
    if a == 1 :
        print("Pile")
    else :
        print("Face")
exo6()

def exo7bis():
    alea = random.randint(0,100)
    print(alea)
    if alea > 75:
        print("face")
    else:
        print("Pile")

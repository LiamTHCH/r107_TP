# -*- coding: utf-8 -*-


##########################################################
# Exercice a
def a(n):
    sum = 0
    for i in range(0,n+1):
        sum = sum + i
    #print(sum)
    return sum

##########################################################
# Exercice b
def b():
    nb = 0
    count = 0
    somme = 0
    while nb < 1:
        nb = int(input("Un nombre :"))

    while somme < nb:
        somme = a(count)
        count = count +1
    print(count-1)

##########################################################
# Exercice c
def c():
    while True:
        if int(input("Un nombre :")) == 100:
            break

##########################################################
# Exercice d
def d():
    liste = []
    for i in range(1,11):
        while True:
            a = int(input("Nombre numero %s :"%(i)))
            if a in range(0,21):
                liste.append(a)
                break
            else:
                print("Le chiffre doit etre en 0 et 20, recomencer.")
    print("Nombre de valeurs inférieur strictement à 10 : %s"%(sum(i<10 for i in liste)))
    print("Nombre de valeurs supérieur à 10 et inférieur strictement à 15 : %s"%(sum(15>i>=10 for i in liste)))
    print("Nombre de valeurs supérieur à 15 : %s"%(sum(i>=15 for i in liste)))


print(a(55))
b()
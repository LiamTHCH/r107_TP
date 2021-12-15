import random
def jeux():
    nb = random.randint(0,100)
    #print(nb)
    nbtour = 0
    j = 0
    while j != nb:
        j = int(input("Un Nombre:"))
        if j<nb:
            print("Trop petit")
            nbtour = nbtour +1
        elif j>nb:
            print("Trop grand")
            nbtour = nbtour +1
        else:
            pass
    print("Bravo, ton nombre d'essaie : %s"% (nbtour+1))
jeux()
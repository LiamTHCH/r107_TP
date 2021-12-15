def factorielle(n):
    if n<2:
        return 1
    else:
        return n*factorielle(n-1)

def factorielfor():
    a = int(input("N! : "))
    somme = int(1)
    if a<2:
        print("= 1")
    else:
        for i in range(a,1,-1):
            somme=i*somme
        print("= ",somme)

def factorielwhile():
    a = int(input("N! : "))
    somme = int(1)
    if a<2:
        print("= 1")
    else:
        while a != 1:
            somme = somme*a
            a = a -1
        print("= ",somme)

factorielfor()
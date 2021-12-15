from calendar import monthrange
date = str(input("Date :"))
dateliste = list(date)
separateur = ""
jours = int(dateliste[0]+dateliste[1])
#jours = int(separateur.join([dateliste[0],dateliste[1]]))
for i in range(0,2):
    dateliste.remove(dateliste[0])

mois = int(separateur.join([dateliste[0],dateliste[1]]))
for i in range(0,2):
    dateliste.remove(dateliste[0])
anne = int(separateur.join(dateliste))
print(jours,mois,anne)
print(monthrange(anne,mois))
if(anne%4==0 and anne%100!=0 or anne%400==0):
    if mois == 2:
        if jours <= 29:
            print("Date valide")
        else:
            print("Date invalide 1")
    elif mois >= 12:
        if jours >= monthrange(anne,mois):
            print("Date valide")
    else:
        print("Date invalide 2")
else:
    if mois <= 12:
        a = monthrange(anne, mois)
        if jours in range(1,a[1]+1):
            print("Date valide")
        else:
            print("Date invalide 3")
    else:
        print("Date invalide 4")

exit(0)


liste = [5,2,4,8,1,3]
print(liste)
for sitem in liste:
    low = sitem
    lowindex = 0
    for i in range(liste.index(sitem),len(liste)):
        if liste[i] < low:
            low = liste[i]
    lowindex = liste.index(low)
    sitemindex = liste.index(sitem)
    liste[lowindex] = sitem
    liste[sitemindex] = low
    print(liste)

print("___________________________________________________")
liste2 = [5,2,4,8,1,3]
liste2.sort()
print(liste2)


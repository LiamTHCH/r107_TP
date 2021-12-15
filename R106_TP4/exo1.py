nb = float(input("Vous cherchez la table de multiplication de quel nombre ?"))
liste = []
for i in range(0,11):
    liste.append(round(i*nb,1))
for i in range(0,len(liste)):
    print("%s * %s =  %s"%(nb,i,liste[i]))

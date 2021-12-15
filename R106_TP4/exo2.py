import statistics
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []
for i in range(1,nombreEtudiants+1):
    notes.append(float(input("Note etudiant %s : "% i)))
moyenne = statistics.mean(notes)
print("Moyenne de classe :",moyenne)
print("Numéro de l’Etudiant | note | ecart a la moyenne ")
for item in notes:
    print("%s | %s | %s"%(notes.index(item),item,(moyenne-item)))



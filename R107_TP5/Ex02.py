note = []
coef = []
temp = []
somenote = 0
somecoef = 0
calc = 0
for i in range(0,10):
    a = input("Veuillez entrer la note du module 1 et le coefficient correspondant : ")
    temp = a.split(" ")
    note.append(float(temp[0]))
    coef.append(float(temp[1]))
for i in range(0,10):
    somenote = somenote + (note[i]*coef[i])
    somecoef = somecoef + coef[i]
calcule = somenote/somecoef
print("Moyenne :",calcule)
if calcule > 8 :
    print("Eleve passe")
else:
    print("Eleve passe pas !!!!!")
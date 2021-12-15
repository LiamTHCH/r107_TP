nMax = 5
v1 = []
v2 = []
n = 0
calc = 0
while not (1 <= n <= nMax):
    n = int(input("Taille effective des vecteurs : "))

for i in range(1,n+1):
    temp = int(input("Composante V1 %s :"%i))
    v1.append(temp)
for i in range(1,n+1):
    temp = int(input("Composante V2 %s :"%i))
    v2.append(temp)
if len(v1) != len(v2):
    print("Erreur Composant")
    exit(2)
for i in range(0,len(v1)):
    calc = calc + (v1[i]*v2[i])
print("Produit scalaire = ",calc)

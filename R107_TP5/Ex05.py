slaireh = 1
try:
    nbh = int(input("Nombre : "))
except ValueError:
    print("Entrez un nombre entier!\n")
    exit(2)
somme = 0
h = [0,0,0]
if 0<nbh<160:
    h[0]=(nbh)
    somme = nbh * slaireh
elif 0<nbh<200:
    h[0]=(160)
    h[1]=(nbh-160)
    somme = (160*slaireh)+(nbh-160)*1.25
elif nbh>250:
    h[0]=(160)
    h[1]=(40)
    h[2]=(nbh-200)
    somme = (160*slaireh)+(40*1.25)+((nbh-200)*1.50)

print("Salaire :",somme)
if h[0] != 0: print(" %s heure(s) au salaire horaire."%(h[0]))
if h[1] != 0: print(" %s heure(s) au salaire horaire 25%%."%(h[1]))
if h[2] != 0: print(" %s heure(s) au salaire horaire 50%%."%(h[2]))

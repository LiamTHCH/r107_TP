import random,string
lettre = string.ascii_letters
T = [random.choice(lettre) for i in range(10)]
T = T + ["w","a","g","o","n"]
T = T + [random.choice(lettre) for i in range(10)]
T = "".join(T)
T = T+"wagon"
T = T.lower()
print(T)
nb = 0
print("Longueur T :",(len(T)))
for i in T:
    if i in "aeiou":
        nb = nb + 1
print("nombre de voyelle : ",nb)
if "wagon" in T:
    print("Wagon dans T en position : ",(T.find("wagon")+1))
    print("Le mot wagon figure %s fois dans la ligne"%(T.count("wagon")))

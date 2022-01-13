__author__ = "Liam Thomas-Chollier RT111"
nb = int(input("Merci de préciser le nombre de lignes :"))
cara = "* "
for i in range(1,nb+1):
    print(i*cara)
print("")

for i in range(nb,-1,-1):
    print((nb-i)*" ",end="")
    print(i*cara)

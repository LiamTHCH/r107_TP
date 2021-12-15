login1 = str(input(" 1e Binome :"))
login2 = str(input(" 2e Binome :"))
binome = tuple([login1,login2]) #Une fois qu'un tuple est créé, vous ne pouvez pas modifier ses valeurs. Les tuples sont inchangeables, ou immuables comme on les appelle aussi.
print("L’étudiant %s est en binome avec l’étudiant %s"% binome)
login2 = str(input("Changer de binome : "))
binome = tuple([login1,login2])
print(binome)
del binome #suprime la variable
login3 = str(input("Nouveau trinome : "))
binome = tuple([login1,login2,login3])
print(binome)

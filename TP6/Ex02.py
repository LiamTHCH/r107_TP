def ajouter_elt(lst, elt):
 lst.append(elt)
 return lst
lst1 = [0,1,2]
lst2 = []
ajouter_elt(lst1,len(lst1))
print(lst1)
print("Type : %s , ID : %s"%(type(lst1),id(lst1)))
print(lst2)
print("Type : %s , ID : %s"%(type(lst2),id(lst2)))
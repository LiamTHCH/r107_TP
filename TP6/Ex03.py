def ajouter_elt(lst=[0,1,2], elt=3):
 lst.append(elt)
 return lst
print(id(ajouter_elt()))
print(id(ajouter_elt()))
def ajouter_carac(ch,elt):
 return ch+elt
print(id(ajouter_elt()))
print(ajouter_carac("abc","d"))
print(id(ajouter_carac("abc","d")))
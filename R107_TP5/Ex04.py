bills = [100,50,10,2,1]

def decompose(amount, bills):
    if not bills:
        return []
    if amount >= bills[0]:
        return [bills[0]] + decompose(amount - bills[0], bills)
    else:
        return decompose(amount, bills[1:])

amount = int(input("Valeur :"))
print("%s €, c'est donc"%(amount),end="")
amountList = list(dict.fromkeys(decompose(amount,bills)))
for item in amountList:
    print(" , ",end="")
    print("%s x %s"%(decompose(amount,bills).count(item),item),end="")


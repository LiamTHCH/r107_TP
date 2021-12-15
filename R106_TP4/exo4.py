L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6,6,7,6,8]


def frequence(List):
    counteur = 0
    num = List[0]

    for i in List:
        freqence_actuel = List.count(i)
        if (freqence_actuel > counteur):
            counteur = freqence_actuel
            num = i

    return num,counteur

print("Le nombre le plus frequent dans la liste est le : %s (%s x)"%frequence(L1))
__author__ = "Liam Thomas-Chollier RT111"
def assurance(age, annee, nbr_accident, anciennete):
    annee_courante = 2022
    if (anciennete < 0) or (nbr_accident<0) or (age<16) or (annee_courante - anciennete < annee) or (annee > annee_courante):
        return 'Anomalie'
    if age < 25:
        if annee_courante - annee < 2:
            if nbr_accident == 0:
                if anciennete > 1:
                    return 'Ornage'
                else:
                    return 'Rouge'
            else:
                return 'Refus'
    elif ((age < 25) and (annee_courante - annee >= 2)) or (((age >= 25) and (annee_courante - annee < 2))):
        if nbr_accident == 0:
            if anciennete > 1:
                return 'Vert'
            else:
                return 'Orange'
        elif nbr_accident == 1:
            if anciennete > 1:
                return 'Ornage'
            else:
                return 'Rouge'
        else:
            return 'Refus'
    elif ((age > 25) and (annee_courante - annee >= 2)):
        if nbr_accident == 1:
            if anciennete > 1:
                return 'Vert'
            else:
                return 'Orange'
        elif nbr_accident == 2:
            if anciennete > 1:
                return 'Ornage'
            else:
                return 'Rouge'
        elif nbr_accident == 0:
            if anciennete > 1:
                return 'Bleu'
            else:
                return 'Vert'
        else:
            return 'Refus'
print(assurance(23,2021,0,0))
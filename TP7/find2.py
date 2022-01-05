import sys
import os

listeFichiers = []
listeDossiers = []

def recherche(dossier):
		os.chdir(dossier)
		liste = os.listdir(dossier)
		for i in liste :
			if os.path.isfile(i):
				listeFichiers.append(dossier + i)
				# elt correspond au dossier à ajouter dans la liste
				# dossier + elt réprésente le chemin complet sur le fichier8
			elif os.path.isdir(i):
				listeDossiers.append(dossier + i)
		print(listeDossiers)
		print("-----------------------")
		print(listeFichiers)


if __name__ == "__main__":
	print(len(sys.argv))
	if len(sys.argv) == 1:
		print("Pas assez d'argument. Ex: find1.py /home")
	else:
		recherche(sys.argv[1])
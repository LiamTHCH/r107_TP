import sys
import os
listeDossiers = []
listeFichiers = []
def aide(msg):
	print(msg)
	exit()
def recherche(dossier, fichier):
	os.chdir(dossier)
	contenuDuRépertoire = os.listdir(dossier)
	for elt in contenuDuRépertoire : # pour chaque élément (elt) du répertoire
		if os.path.isdir(elt) : # si c’est un dossier
			listeDossiers.append(dossier +"/"+ elt)
		elif os.path.isfile(elt) : # sinon si c’est un fichier
			if elt == fichier : # si c’est le même de fichier
				listeFichiers.append(dossier +"/"+ elt)

if __name__ == '__main__':
	if len(sys.argv) > 6 : # mauvais nombre d’arguments
		aide("Mauvais nombre d’arguments")
	else:
		dossier = ""
		fichier = ""
	for i in range(1,len(sys.argv)): # je recherche les arguments
		if sys.argv[i] == "-d":
			dossier = sys.argv[i+1]
		elif sys.argv[i] == "-f":
			fichier = sys.argv[i+1]
	if not os.path.exists(dossier) : # si le dossier n’existe pas
		aide("Donniser n'existe pas")
	else :
		if len(os.listdir(dossier) ) == 0: # si dossier ou fichier sont vides
			aide("Dossier vide")
		else:
			listeDossiers.append(dossier)
			for dos in listeDossiers:
				recherche(dos, fichier)
			for fiche in listeFichiers :
				print(fiche)
import sys
import os
					
def affiche(dir):
	if os.path.exists(dir):
		os.chdir(dir)
		for item in os.listdir(dir):
			print(item)
	else:
		print("Dossier inexistant")
if __name__ == "__main__":
	print(len(sys.argv))
	if len(sys.argv) == 1:
		print("Pas assez d'argument. Ex: find1.py /home")
	else:
		affiche(sys.argv[1])
import sys
if __name__ == '__main__':
	print(len(sys.argv))
	if len(sys.argv) == 1:
		print("pas assez d’arguments pour le script",sys.argv[0])
	else:
		for ar in sys.argv:
			print(ar)

# S'occupe de la création des MDP potentiels avec les saisies utilisateurs.
import re

class Chimiste() :
	def __init__(self, potentiel) :
		self.potentiel = potentiel
		self.infinite = []

	# Modifie les mots avec le LEET
	def LEET(self) :
		pass #rint(self.potentiel)

	# Ajoute beaucoup de nombres.
	def Infinity(self) :

		print("\nNombre limite par défaut = 100 000")
		limite = input("Définir votre limite ? : ")

		if limite == "" :
			limite = 100_000

		compteur = 0
		while compteur <= int(limite) :
			for k in range(len(self.potentiel)) :
				self.infinite.append(self.potentiel[k] + str(compteur))
			compteur += 1
			
		for element in self.infinite:
			self.potentiel.append(element)

		print(self.infinite)
		return self.infinite

	def setPotentiel(self, potentiel) :
		self.potentiel = potentiel

	def getPotentiel(self) :
		return self.potentiel

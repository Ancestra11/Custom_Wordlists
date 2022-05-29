# S'occupe de la création des MDP potentiels avec les saisies utilisateurs.
import re

class Chimiste() :
	def __init__(self, potentiel) :
		self.potentiel = potentiel

	def Modifications(self) :
		print(self.potentiel)
		
	def setPotentiel(self, potentiel) :
		self.potentiel = potentiel

	def getPotentiel(self) :
		return self.potentiel

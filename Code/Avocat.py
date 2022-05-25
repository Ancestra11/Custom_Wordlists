#Contrôle si les saisies utilisateurs sont valables.

class Avocat() :
    def __init__(self, message, *limitation) :
        self.message = message
        self.limitation = limitation
        self.keywords = keywords

    def Controle(self) :
        self.keywords = ['s', 'a', 'r']
        for k in range(len(self.keywords)) :
            if self.keywords[k] in self.limitation :
                print("a ba ",k," oui")
            else :
                print("pala", k)

Avoc = Avocat("Hello, friend.", 1, 's', 3, "test4")
Avoc.Controle()

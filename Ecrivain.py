print("Saisir un mot servant pour le dictionnaire de mots de passe")
print("(0 = STOP) : ")

class Ecrivain() :
    def __init__(self):
        self.continuer = True
        self.potentiel = []

    def Collecte(self) :
        #continuer = True

        while self.continuer :
            ajouts = input()
            self.potentiel.append(ajouts)

            if ajouts == '0' :
                print("\nStopper la saisie ? Ou ajouter '0' dans le dictionnaire ?")
                confirm = input("S = Stop, A = Ajout, R = Retour) : ")
                self.Arret(confirm)


    def Arret(self, confirm) :
        if confirm.upper() == 'S' :
            self.potentiel.pop()
            self.continuer = False
        elif confirm.upper() == 'A' :
            self.potentiel.append(ajouts)
        elif confirm.upper() == 'R' :
            pass
        else :
            Arret(confirm)
        return self.continuer
        
    def Ecriture(self) :
        NomFichier = input("\nQuel nom donner au fichier ? ")

        with open(NomFichier, 'w') as Fichier :
            for items in self.potentiel :
                Fichier.write('%s\n' %items)

#main = Ecrivain()
#main.Collecte()
#main.Ecriture()

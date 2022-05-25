print("Saisir un mot servant pour le dictionnaire de mots de passe")
print("(0 = STOP) : ")

class Ecrivain() :
    def __init__(self):
        self.continuer = True
        self.potentiel = []

    def Collecte(self) :

        while self.continuer :
            self.ajouts = input()
            self.potentiel.append(self.ajouts)

            if self.ajouts == '0' :
                print("\nStopper la saisie ? Ou ajouter '0' dans le dictionnaire ?")
                self.confirm = input("S = Stop, A = Ajout, R = Retour) : ")
                self.Arret(self.confirm)


    def Arret(self, confirm) :
        #SaisieUtilisateur = True
        while SaisieUtilisateur :
            #SaisieUtilisateur = False
            if self.confirm.upper() == 'S' :
                self.potentiel.pop()
                self.continuer = False
            elif self.confirm.upper() == 'A' :
                pass
            elif self.confirm.upper() == 'R' :
                self.potentiel.pop()
            #else :
                #SaisieUtilisateur = True
        return self.continuer
        

    def Ecriture(self) :
        print("\nNom par défaut = 'Exemple.txt' ") 
        NomFichier = input("Donner un autre nom au fichier ? : ")

        if NomFichier == "" :
            NomFichier = "Exemple.txt"

        with open(NomFichier, 'w') as Fichier :
            for items in self.potentiel :
                Fichier.write('%s\n' %items)

    def getPotentiel(self) :
        return self.potentiel
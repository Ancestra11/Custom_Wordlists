potentiel = []

print("Saisir un mot servant pour le dictionnaire de mots de passe (0 = STOP) : ")

def Collecte() :
    continuer = True

    while continuer :
        ajouts = input()
        potentiel.append(ajouts)

        if ajouts == '0' :
            confirm = input("\nStopper la saisie ? Ou ajouter '0' dans le dictionnaire ? \n(S = Stop, A = Ajout, R = Retour) : ")

            if confirm == 'S' :
                potentiel.pop()
                continuer = False
            elif confirm == 'A' :
                potentiel.append(ajouts)
            elif confirm == 'R' :
                continue
        

print(potentiel)

def Ecriture() :
    NomFichier = input("\nQuel nom donner au fichier ? ")

    with open(NomFichier, 'w') as Fichier :
        for items in potentiel :
            Fichier.write('%s\n' %items)

Collecte()
Ecriture()

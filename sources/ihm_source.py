from laboratoire import *

'''
Interface sur la labo avec menu textuel.
'''

def afficher_menu():
    print('1- Enregistrer une arrivée')
    print('2- Présence d\'une personne')
    print('0- Quitter')

def demander_choix():
    return int(input("Votre choix: "))

def gerer_arrivee(labo):
        try:
            nom = input("Nom ? ")
            bureau = input("Bureau ? ")
            enregistrer_arrivee(labo, nom, bureau)
        except ValueError:
            print("Impossible: déja là")

def traiter_choix(choix, labo):
    if choix == 1:
        gerer_arrivee(labo)
    elif choix == 2:
        nom = input("Nom ? ")
        reponse = est_presente(labo, nom)
        print('oui, présente' if reponse else 'non, inconnue')




def main():
    quitter = False
    labo = laboratoire()
    while not quitter:
        afficher_menu()
        choix = demander_choix()
        traiter_choix(choix, labo)
        print(labo)
        quitter = choix == 0


if __name__ == '__main__':
    main()

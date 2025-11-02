from laboratoire import *

'''
Interface sur la labo avec menu textuel.
'''

def afficher_menu():
    print('1- Enregistrer une arrivée')
    print('2- Présence d\'une personne')
    print('3- Enregistrer un départ')
    print("4- Modifier le bureau d'une personne")
    print("5- Changer le nom d'une personne")
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


def gerer_depart(labo):
    try: 
        nom = input("Nom ? ")
        enregistrer_depart(labo, nom)
    except AbsentException:
        print("Déjà parti")


def gerer_bureau(labo):
    nom = input("Nom ? ")
    bureau = input("Bureau ? ")
    changer_bureau(labo, nom, bureau)


def modification_nom(labo):
    nom = input("Personne à modifier ? ")
    nouveau_nom = input("Nouveau nom ? ")
    changer_nom(labo, nom, nouveau_nom)



def traiter_choix(choix, labo):
    if choix == 1:
        gerer_arrivee(labo)
    elif choix == 2:
        nom = input("Nom ? ")
        reponse = est_presente(labo, nom)
        print('oui, présente' if reponse else 'non, inconnue')
    elif choix == 3:
        gerer_depart(labo)
    elif choix == 4:
        gerer_bureau(labo)
    elif choix == 5:
        modification_nom(labo)




def main():
    quitter = False
    labo = laboratoire()
    while not quitter:
        afficher_menu()
        choix = demander_choix()
        traiter_choix(choix, labo)
        print(labo)
        quitter = choix == 0
        print()



if __name__ == '__main__':
    main()

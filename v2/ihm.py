'''
Interface gestion du laboratoire
'''

from laboratoire import *
import os 

#Fonctionne du gestionnaire de laboratoire
def gerer_arrivee(labo):
        try:
            nom = input("Nom ? ")
            bureau = input("Bureau ? ")
            enregistrer_arrivee(labo, nom, bureau)
            write_as_json(labo, "laboratoire.json")
        except ValueError:
            print("Impossible: déja là")


def presence(labo):
    nom = input("Nom ? ")
    reponse = est_presente(labo,nom)
    print("oui, présent" if reponse else "non, inconnue")


def gerer_depart(labo):
    try: 
        nom = input("Nom ? ")
        enregistrer_depart(labo, nom)
        print(f"{nom} a été retiré du laboratoire")
        write_as_json(labo, "laboratoire.json")
    except AbsentException:
        print(f"{nom} n'existe pas dans le laboratoire")


def gerer_bureau(labo):
    try:
        nom = input("Nom ? ")
        bureau = input("Bureau ? ")
        changer_bureau(labo, nom, bureau)
        write_as_json(labo, "laboratoire.json")
    except AbsentException:
        print(f"{nom} n'existe pas")
    

def modification_nom(labo):
    try:
        nom = input("Personne à modifier ? ")
        nouveau_nom = input("Nouveau nom ? ")
        changer_nom(labo, nom, nouveau_nom)
        write_as_json(labo, "laboratoire.json")
    except AbsentException:
        print(f"{nom} n'existe pas")


def connaitre_bureau(labo):
    nom = input("Nom ? ")
    bureau = nom_bureau(labo, nom)
    print(f"{nom} est dans le bureau {bureau}")


def afficher_listing(labo):
    labo_inverse = inverse_dictionnaire(labo)
    for bureau, nom in sorted(labo_inverse.items()):
        print(f"{bureau:2} :")
        for elt in nom:
            print(f"- {elt}", sep="\n")
    
    ecrire_labo_html(labo_inverse)
    write_as_json(labo_inverse, "laboratoire_ordered.json")


def import_json(labo):
    path = "laboratoire.json"
    if os.path.exists(path):
        try:
            load_json(labo, path)
        except json.JSONDecodeError:
            pass
    else:
        return labo 




def import_from_csv(labo):
    file = input("Nom de fichier ? ")
    modify_dict_csv(labo, file)





#Gestion du menu du gestionnaire de laboratoire 
def Menu():
    return list()


def ajouter_options(menu, name, fonction, *parameters):
    menu.append( (name, fonction, parameters) )


def populate_menu(menu):
    ajouter_options(menu, "Enregistrer une arrivée", gerer_arrivee)
    ajouter_options(menu, "Présence d'une personne", presence)
    ajouter_options(menu, "Enregistrer un départ", gerer_depart)
    ajouter_options(menu, "Modifier le bureau d'une personne", gerer_bureau)
    ajouter_options(menu, "Changer le nom d'une personne", modification_nom)
    ajouter_options(menu, "Connaitre le bureau d'une personne", connaitre_bureau)
    ajouter_options(menu, "Listing laboratoire", afficher_listing)
    ajouter_options(menu, "Importer depuis un fichier csv", import_from_csv)


def traiter_choix(menu, choix):
    assert 0 <= choix <= len(menu)
    if choix != 0:
        _, fonction, parameters = menu[choix -1]
        fonction(labo, *parameters)


def selection(menu):
	while True:
            try:
                numero = int(input("Votre choix ? "))   #Récupérer le choix de l'utilisateur 
                if 0 <= numero <= len(menu):   #Le choix doit être compris entre 0 et la longueur du menu
                    return numero
                else: 
                    print("Pas un numéro du menu")
            except ValueError:
                print("Incorrect...")


def afficher(menu):
	for numero, (intitule, _, _) in enumerate(menu, 1):
		print(f"{numero:2d}- {intitule}")
	print(f"{0:2}- Quitter")
      

def gerer(menu):
    fini = False
    while not fini:
        afficher(menu)
        choix = selection(menu)
        print()
        traiter_choix(menu, choix)
        fini = choix == 0
        print()
    
    print("Fermeture du gestionnaire de Laboratoire")


if __name__ == "__main__":
     
    menu = Menu()
    labo = laboratoire()
    import_json(labo)
    populate_menu(menu)
    gerer(menu)
    
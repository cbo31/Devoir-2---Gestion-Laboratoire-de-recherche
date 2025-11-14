'''
Interface gestion du laboratoire
'''

from laboratoire import *
from menus import*
import os 

#Fonctionne du gestionnaire de laboratoire
def gerer_arrivee(labo):
        try:
            nom = input("Nom ? ")
            bureau = input("Bureau ? ")
            enregistrer_arrivee(labo, nom, bureau)
            write_as_json(labo, "laboratoire.json")
            print(f"{nom} a bien été enregistré")
        except PresentException:
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
        print(f"Le bureau de {nom} a bien été modifié")
    except AbsentException:
        print(f"{nom} n'existe pas")
    

def modification_nom(labo):
    try:
        nom = input("Personne à modifier ? ")
        nouveau_nom = input("Nouveau nom ? ")
        changer_nom(labo, nom, nouveau_nom)
        write_as_json(labo, "laboratoire.json")
        print(f"{nom} a été modifié par {nouveau_nom}")
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
    file = input("Nom de fichier ? ") + ".csv"
    csv_dict = load_csv(file)
    for csv_nom, csv_bureau in csv_dict.items():
        try:
            enregistrer_arrivee(labo, csv_nom, csv_bureau)
        except:
            print(f"{csv_nom} déjà présent dans le laboratoire")    
    
    write_as_json(labo, "laboratoire.json")





#Gerer option du menu
def populate_menu(menu):
    ajouter_options(menu, "Enregistrer une arrivée", gerer_arrivee, labo)
    ajouter_options(menu, "Présence d'une personne", presence, labo)
    ajouter_options(menu, "Enregistrer un départ", gerer_depart, labo)
    ajouter_options(menu, "Modifier le bureau d'une personne", gerer_bureau, labo)
    ajouter_options(menu, "Changer le nom d'une personne", modification_nom, labo)
    ajouter_options(menu, "Connaitre le bureau d'une personne", connaitre_bureau, labo)
    ajouter_options(menu, "Listing laboratoire", afficher_listing, labo)
    ajouter_options(menu, "Importer depuis un fichier csv", import_from_csv, labo)


if __name__ == "__main__":
     
    menu = Menu()
    labo = laboratoire()
    import_json(labo)
    populate_menu(menu)
    gerer(menu)
    print("Fermeture du gestionnaire de Laboratoire")
    
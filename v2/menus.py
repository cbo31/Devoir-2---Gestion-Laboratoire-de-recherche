#Gestion du menu du gestionnaire de laboratoire 
def Menu():
    return list()


def ajouter_options(menu, name, fonction, labo, *parameters):
    menu.append( (name, fonction, labo, parameters) )


def traiter_choix(menu, choix):
    assert 0 <= choix <= len(menu)
    if choix != 0:
        _, fonction, labo, parameters = menu[choix -1]
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
	for numero, (intitule, _, _, _) in enumerate(menu, 1):
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



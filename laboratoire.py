'''
Les opérations sur le laboratoire sans interactions avec l'utilisateur.
Pas de input, pas de print.
Backend.
Partie réutilisable entre les différentes IHM.
python labo_cmd.py add Xavier F305
'''

# Définir ce qu'est un laboratoire ? Quel type ?

# Réponse : dictionnaire, clé = personne, valeur = bureau

'''
Evolution possible :
    labo = {
        'bureaux' : {
            'F305': 4,
            'F307': 2,
        },
        'affectations': {
            'Xavier': 'F305',
        }

    }
'''

# Les choix faits ici, ne devraient pas être utilisés à l'extérieur.

class LaboException(Exception):
    pass

class AbsentException(LaboException):
    pass

class PresentException(LaboException):
    pass


def laboratoire():
    return {}

def enregistrer_arrivee(labo, nom, bureau):
    if nom in labo:
        raise ValueError
    labo[nom] = bureau

def enregistrer_depart(labo, nom):
    if not nom in labo:
        raise AbsentException
    labo.pop(nom)

def changer_bureau(labo, nom, bureau):
    if not nom in labo:
        raise AbsentException
    labo[nom] = bureau

def changer_nom(labo, nom, nouveau_nom):
    if not nom in labo:
        raise AbsentException
    value = labo.pop(nom)
    labo[nouveau_nom] = value

def est_presente(labo, nom):
    return nom in labo

def nom_bureau(labo, nom):
    if nom in labo:
        return labo.get(nom)


    
    

    

# Les opérations qui permettent de manipuler les données du labo.

def main():
    print('test')

if __name__ == '__main__':
    main()

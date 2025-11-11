'''
Fonctionnalités du laboratoire
'''


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
    

def inverse_dictionnaire(labo):
    temp_dict = dict()
    for nom, bureau in sorted(labo.items()):
        temp_dict.setdefault(bureau, []).append(nom)
    return temp_dict


def ecrire_labo_html(labo):
    file_path = "/Users/clement/Documents/Formation_DU_FullStack/devoirs/Python/Devoir2/devoir-2-gestion-laboratoire-de-recherche/v2/laboratoire.html"
    corps = f"""<body>
                    <h1>Laboratoire</h1>
                    <h2>Personnel</h2>
                </body>
            """
            
    with open(file_path, "w") as file:
        file.write(corps)
        for bureau,nom in labo.items():
            t = f"""<p>
                        {bureau:2} :
                    </p>
                """
            file.write(t)
            for elt in nom:
                e = f"""
                        <p>
                            - {elt:2}
                        </p>
                    """
                file.write(e)

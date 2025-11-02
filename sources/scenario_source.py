from laboratoire import *

def main():
    labo = laboratoire()
    enregistrer_arrivee(labo, 'Xavier', 'F305')
    enregistrer_arrivee(labo, 'Marc', 'F305')
    print(labo)
    assert est_presente(labo, 'Xavier')
    assert est_presente(labo, 'Marc')
    assert not est_presente(labo, 'Aurélie')
    # assert bureau(labo, 'Xavier') == 'F305'


if __name__ == '__main__':
    main()

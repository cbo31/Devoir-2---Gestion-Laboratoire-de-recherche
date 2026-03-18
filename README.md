# 🔬 Devoir 2 — Gestion de Laboratoire de Recherche

> Exercice Python · Architecture Frontend / Backend · Interface en ligne de commande

---

## 📖 Présentation

Ce projet est un exercice Python sur la **séparation des responsabilités** entre frontend et backend. L'application permet de gérer les présences et les affectations de bureau des membres d'un laboratoire de recherche, via une **interface en ligne de commande** (terminal).

La structure du code illustre un principe fondamental du développement logiciel :

- **`laboratoire.py`** — le backend : toutes les opérations sur les données, sans aucune interaction utilisateur (`input`, `print`)
- **`ihm.py`** — le frontend : le menu interactif dans le terminal, qui appelle les fonctions du backend
- **`scenario.py`** — des scénarios de test

---

## 🗂️ Structure du projet

```
Devoir-2---Gestion-Laboratoire-de-recherche/
├── laboratoire.py       # Backend — logique métier (dictionnaire nom → bureau)
├── ihm.py               # Frontend — interface utilisateur en terminal
├── scenario.py          # Scénarios de test
├── ihm_raffinage.txt    # Notes de conception de l'IHM
├── labo_raffinage.txt   # Notes de conception du backend
├── sources/             # Fichiers sources complémentaires
├── v2/                  # Version 2 du projet
└── README.md
```

---

## ⚙️ Fonctionnalités

L'application propose un menu à 8 options :

| Option | Action |
|--------|--------|
| `1` | Enregistrer une arrivée (nom + bureau) |
| `2` | Vérifier la présence d'une personne |
| `3` | Enregistrer un départ |
| `4` | Modifier le bureau d'une personne |
| `5` | Changer le nom d'une personne |
| `6` | Connaître le bureau d'une personne |
| `7` | Afficher le listing du laboratoire + export HTML |
| `0` | Quitter |

---

## 🏗️ Architecture

Le laboratoire est modélisé par un **dictionnaire Python** : `{ nom: bureau }`.

```python
labo = {
    'Alice': 'F305',
    'Bob':   'F307',
}
```

### Backend — `laboratoire.py`

Fonctions disponibles, sans aucune interaction utilisateur :

- `laboratoire()` — crée un labo vide
- `enregistrer_arrivee(labo, nom, bureau)` — ajoute une personne
- `enregistrer_depart(labo, nom)` — retire une personne
- `changer_bureau(labo, nom, bureau)` — modifie l'affectation
- `changer_nom(labo, nom, nouveau_nom)` — renomme une personne
- `est_presente(labo, nom)` → `bool`
- `nom_bureau(labo, nom)` → numéro de bureau
- `inverse_dictionnaire(labo)` — regroupe par bureau
- `ecrire_labo_html(labo)` — exporte le listing en HTML

### Exceptions personnalisées

```python
class LaboException(Exception): pass
class AbsentException(LaboException): pass  # personne introuvable
class PresentException(LaboException): pass # personne déjà présente
```

---

## 🚀 Lancement

### Prérequis

- Python 3.x (aucune dépendance externe)

### Démarrer l'application

```bash
python ihm.py
```

Le menu s'affiche dans le terminal, il suffit de saisir le numéro de l'option souhaitée.

---

## 📝 Notes

- Ce projet est réalisé dans le cadre de la formation **DU Fullstack**.
- L'export HTML (`option 7`) génère un fichier `laboratoire.html` — le chemin de sortie est à adapter selon votre environnement.
- Le dossier `v2/` contient une version améliorée du projet.

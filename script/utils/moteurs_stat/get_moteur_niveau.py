

from pilotage import load_arbre


def get_moteur_niveau(moteur: str, periodicite: str) -> str:
    arbre = load_arbre(periodicite)
    for niveau in arbre.keys():
        if moteur in  arbre[niveau].keys():
            return niveau

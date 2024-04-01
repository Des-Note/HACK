# calculatrice.py

import re

def calculatrice(expression):
    try:
        # Supprime les caractères non numériques, sauf les opérateurs mathématiques
        expression = re.sub(r'[^\d+\-*/().]', '', expression)
        # Évalue l'expression mathématique
        resultat = eval(expression)
        return resultat
    except Exception as e:
        return "Erreur: " + str(e)

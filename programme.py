"""
Un script Python qui requiert trois arguments : le premier spécifiant l'opération souhaitée et les deux suivants étant 
les deux entiers sur lesquels effectuer cette opération.
"""

import calculatrice
import sys


print("Bienvenue dans cette petite calculatrice Python des nombres réels.\n")

def executer_calculatrice():
    operation = input("Choisissez une opération parmi +, -, *, / et % : \n")
    nbre1 = input("Entrez le premier nombre : \n")
    nbre2 = input("Entrez le deuxième nombre : \n")
    resultat = calculatrice.operation(operation, nbre1, nbre2)
    if resultat is not None:
        print("{} {} {} = {}".format(nbre1, operation, nbre2, resultat))
        continuer = input("Voulez-vous arrêter le programme ? Si oui, écrivez 'Oui'. Sinon, appuyez sur Entrée.\n")
        if continuer.lower() == "oui":
            sys.exit(0)
    print("Nous allons recommencer le programme.\n")
    executer_calculatrice()

executer_calculatrice()

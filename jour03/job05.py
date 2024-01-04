# -*- coding: utf-8 -*-
"""
Made by: Raphael
Email: raphael.attias@laplateforme.io
"""

import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté du combat (1, 2 ou 3): "))

    def lancerJeu(self):
        self.choisirNiveau()
        vie_joueur = self.niveau * 10
        vie_ennemi = self.niveau * 15

        joueur = Personnage("Prince", vie_joueur)
        ennemi = Personnage("Dragon", vie_ennemi)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu! C'est gagné!")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu! C'est perdu.")
                break

            print(f"\nStats actuelles - {joueur.nom}: {joueur.vie} pv, {ennemi.nom}: {ennemi.vie} pv.\n")


if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancerJeu()

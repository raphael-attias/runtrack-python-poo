# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} ({self.position}, numéro {self.numero}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons Jaunes: {self.cartons_jaunes}")
        print(f"Cartons Rouges: {self.cartons_rouges}")
        print("\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton Jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton Rouge":
                    joueur.recevoirUnCartonRouge()
                else:
                    print("Autre Action.")
                break


equipe1 = Equipe("OM")
equipe2 = Equipe("PSG")

joueur1 = Joueur("SARR", 10, "Attaquant")
joueur2 = Joueur("RONGIER", 7, "Milieu")
joueur3 = Joueur("kk", 5, "Défenseur")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur("SARR", "but")
equipe2.mettreAJourStatistiquesJoueur("kk", "carton_rouge")

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

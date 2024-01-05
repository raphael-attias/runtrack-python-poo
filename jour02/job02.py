# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Livre:
    def __init__(self, titre, auteur, nbrpages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbrpages = nbrpages
    
    # les assesseurs
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nbrpages(self):
        return self.__nbrpages
    
    # les mutateurs
        
    def set_nbrpages(self, nbrpages):
        if type(nbrpages) == int and nbrpages > 0:
            self.__nbrpages = nbrpages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

livre_a = Livre("Les Forceurs de blocus", "Jules Verne", 96)

print("Titre du livre :", livre_a.get_titre())
print("Auteur du livre :", livre_a.get_auteur())
print("Nombre de pages du livre :", livre_a.get_nbrpages())
print()

livre_a.set_nbrpages(100)

print("Données du livre mis à jour : ")
print("Titre du livre :", livre_a.get_titre())
print("Auteur du livre :", livre_a.get_auteur())
print("Nouveau nombre de pages du livre :", livre_a.get_nbrpages())

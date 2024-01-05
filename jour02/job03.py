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
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nbrpages(self):
        return self.__nbrpages

    def is_disponible(self):
        return self.__disponible

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nbrpages(self, nombre_pages):
        if type(nombre_pages) == int and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Le nombre de pages doit être un entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.__disponible:
            print("Le livre est disponible. Emprunt possible.")
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.__disponible:
            print("Le livre va etre rendu.")
            self.__disponible = True
        else:
            print("Le livre est déjà disponible.")

mon_livre = Livre("Titre du Livre", "Auteur du Livre", 200)

print(f"Disponible : {mon_livre.verification()}")

mon_livre.emprunter()

print(f"Disponible : {mon_livre.verification()}")

mon_livre.rendre()

print(f"Disponible : {mon_livre.verification()}")

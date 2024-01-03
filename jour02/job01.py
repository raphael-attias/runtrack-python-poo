# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    # Les assenceurs    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    # Les mutateurs
    def set_largeur(self, largeur):
        self.__largeur = largeur
        
    def set_longueur(self, longueur):
        self.__longueur = longueur

rect = Rectangle(10,5)

print("Longueur du rectangle :", rect.get_longueur())
print("Largeur du rectangle :", rect.get_largeur())

# nouvelle valeur du rectagle grâce au set
rect.set_largeur(8)
rect.set_longueur(6)

print("Longueur du rectangle :", rect.get_longueur())
print("Largeur du rectangle :", rect.get_largeur())
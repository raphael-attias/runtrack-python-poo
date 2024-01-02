# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

animal = Animal()

print("L'âge initial de l'animal est :", animal.age)

animal.vieillir()

print("L'âge après la méthode vieillir est :", animal.age)

animal.nommer("Luna")

print("L'animal se nomme :", animal.prenom)

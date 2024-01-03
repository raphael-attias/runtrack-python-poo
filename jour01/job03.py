# -*- coding: utf-8 -*-
"""
Made in Marseille

@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Operation:
    def __init__(self, nombre1=1, nombre2=22):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        return resultat

variables_doper = Operation()

print("le nombre 1 est :", variables_doper.nombre1)
print("le nombre 2 est :", variables_doper.nombre2)
print("l'addition est : ", variables_doper.addition())

# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Personnage:
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
       self.x += 1

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def position(self):
        return self.x, self.y
    
personnage = Personnage()

print("Position initiale :", personnage.position())

personnage.droite()
print("Position Droite :", personnage.position())

personnage.bas()
print("Position Bas :", personnage.position())

personnage.haut()
print("Position Haut :", personnage.position())

personnage.gauche()
print("Position Gauche :", personnage.position())

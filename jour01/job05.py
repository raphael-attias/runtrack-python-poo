# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def AfficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")
    
    def AfficherX(self):
        print(f"La coordonnée X est : {self.x}")
    
    def AfficherY(self):
        print(f"La coordonnée Y est : {self.y}")
    
    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

point = Point(3, 4)

# les méthodes utilisés
point.AfficherLesPoints()
point.AfficherX()
point.AfficherY()
point.changerX(7)
point.changerY(10)
point.AfficherLesPoints()

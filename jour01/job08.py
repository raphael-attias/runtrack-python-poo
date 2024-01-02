# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

for cercle in [cercle1, cercle2]:
    print(f"La circonférence du cercle est : {cercle.circonference()}")
    print(f"Le diamètre du cercle est : {cercle.diametre()}")
    print(f"L'Aire du cercle est : {cercle.aire()}\n")

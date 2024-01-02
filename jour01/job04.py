# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        # Concaténation de la chaîne (+ xxxx +)
        return "Je suis " + self.nom + " " + self.prenom


personne1 = Personne("Doe", "John")
personne2 = Personne("Dupont", "Jean")


print(personne1.SePresenter())
print(personne2.SePresenter())

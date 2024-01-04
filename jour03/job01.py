# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Ville:
    def __init__(self, nom, nbr_hab):
        self.nom = nom
        self.nbr_hab = nbr_hab
    
    def get_total(self):
        return self.nom, self.nbr_hab
       
class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.ville = ville
        
    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age
    
    def habite_a(self):
        return self.ville
    
    def ajouterPopulation(self):
        self.ville.nbr_hab += 1

ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)

habitant1 = Personne("John", 45, ville1)
habitant2 = Personne("Myrtille", 4, ville1)
habitant3 = Personne("Chloé", 18, ville2)

print("Population de la ville de", ville1.get_total())
print("Population de la ville de", ville2.get_total())

habitant1.ajouterPopulation()
habitant2.ajouterPopulation()
habitant3.ajouterPopulation()

print("Population de la ville de", ville1.get_total(), "après l'arrivée des nouveaux habitants.")
print("Population de la ville de", ville2.get_total(), "après l'arrivée des nouveaux habitants.")

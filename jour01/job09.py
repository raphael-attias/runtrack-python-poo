# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA / 100 

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)

    def ObtenirInformations(self):
        informations = f"Nom du produit : {self.nom}\n"
        informations += f"Prix HT : {self.prixHT} €\n"
        informations += f"TVA : {self.TVA * 100}%\n"
        informations += f"Prix TTC : {self.calculerPrixTTC()} €"
        return informations

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

produit1 = Produit("Produit_X", 10, 20)
produit2 = Produit("Produit_Y", 20, 15)

informations_produit1 = produit1.ObtenirInformations()
informations_produit2 = produit2.ObtenirInformations()

print("Informations initiales des produits :")
print(informations_produit1)
print(informations_produit2)

produit1.modifierNom("Nouveau Produit_X")
produit1.modifierPrix(15)

produit2.modifierNom("Nouveau Produit_Y")
produit2.modifierPrix(25)

# Obtention prix après TVA
informations_modifiees_produit1 = produit1.ObtenirInformations()
informations_modifiees_produit2 = produit2.ObtenirInformations()

print("Informations des produits après TVA :")
print(informations_modifiees_produit1)
print(informations_modifiees_produit2)

# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if self.__statut_commande == "en cours":
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")

    def annuler_commande(self):
        if self.__statut_commande == "en cours":
            self.__plats_commandes.clear()
            self.__statut_commande = "annulée"
            print("Commande annulée.")

    def calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values() if plat["statut"] == "en cours")
        return total

    def afficher_commande(self):
        print(f"Commande #{self.__numero_commande} - Statut: {self.__statut_commande}")
        for nom_plat, plat in self.__plats_commandes.items():
            print(f"{nom_plat}: {plat['prix']} € - Statut: {plat['statut']}")
        total = self.calculer_total()
        print(f"Total à payer: {total} €")

    def calculer_tva(self):
        total = self.calculer_total()
        tva = total * 0.2
        return tva


commande_a = Commande(1)

commande_a.ajouter_plat("Pizza", 12.5)
commande_a.ajouter_plat("Pâtes", 8.0)
commande_a.ajouter_plat("Salade", 5.5)

commande_a.afficher_commande()
print(f"TVA: {commande_a.calculer_tva()} €")

commande_a.annuler_commande()
commande_a.afficher_commande()

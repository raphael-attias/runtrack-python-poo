# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde, decouvert=False):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def get_num_compte(self):
        return self.__num_compte
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde

    def afficher(self):
        return f"Numéro de compte: {self.__num_compte}, Nom: {self.__nom}, Prénom: {self.__prenom}, Solde: {self.__solde}€, Découvert autorisé: {self.__decouvert}"
    
    def afficherSolde(self):
        return f"Solde actuel: {self.__solde}€"
    
    def versement(self, montant):
        self.__solde += montant
        return f"Versement de {montant}€ validé. Nouveau solde: {self.__solde}"
    
    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            return f"Retrait de {montant}€ validé. Nouveau solde: {self.__solde}"
        else:
            return "Pas assez de fonds sur le compte. Opération non valide."

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios_amount = abs(self.__solde) * taux_agios
            self.__solde -= agios_amount
            return f"Agios appliqués. Nouveau solde: {self.__solde}€"
        else:
            return "Pas d'agios nécessaires. Solde positif."

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            return f"Virement de {montant}€ validé sur le compte {compte_destinataire.get_num_compte()}. Nouveau solde: {self.__solde}€"
        else:
            return "Pas assez de fonds sur le compte. Virement non valide."

compte_alex = CompteBancaire("FRA1726892", "TERIEUR", "Alex", 5)

print(compte_alex.afficher())

compte_alain = CompteBancaire("FRA1726893", "TERIEUR", "Alain", -50, decouvert=True)# ici decouvert autorisé car ajout de valeur booleen

print(compte_alain.afficher())

versement_vers_compte2 = 70
print(compte_alex.virement(compte_alain, versement_vers_compte2))

print("Solde du compte de alex TERIEUR après virement:", compte_alex.afficherSolde())
print("Solde du compte de alain TERIEUR après virement:", compte_alain.afficherSolde())

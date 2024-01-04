# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def total(self):
        return f"{self.titre} ; {self.description} : {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                return f"Tâche '{titre}' supprimée."
        return f"Tâche '{titre}' introuvable."

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Fait"
                return f"Tâche '{titre}' marquée comme 'Fait'."
        return f"Tâche '{titre}' introuvable."

    def afficherListe(self):
        return [tache.total() for tache in self.taches]

    def filterListe(self, statut):
        return [tache.total() for tache in self.taches if tache.statut == statut]

tache1 = Tache("Faire les courses", "recuperer le drive")
tache2 = Tache("Réviser Python", "Faire les jobs du jour 3")
tache3 = Tache("Sport", "Préparer les affaires de voiles")
liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

print("Liste :")
for tache in liste_taches.afficherListe():
    print(tache)

liste_taches.marquerCommeFinie("Faire les courses")
liste_taches.supprimerTache("Réviser Python")

print("\nListe mise à jour:")
for tache in liste_taches.afficherListe():
    print(tache)

taches_a_faire = liste_taches.filterListe("À faire")
print("\nTâches à faire:")
for tache in taches_a_faire:
    print(tache)

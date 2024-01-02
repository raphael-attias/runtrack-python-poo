class Personnage:
    def __init__(self, x=0, y=0, taille_plateau=5):
        self.x = x
        self.y = y
        self.taille_plateau = taille_plateau
        self.plateau = [['.' for _ in range(taille_plateau)] for _ in range(taille_plateau)]
        self.plateau[x][y] = 'P'  

    def gauche(self):
        if self.x > 0:
            self.plateau[self.x][self.y] = '.'
            self.x -= 1
            self.plateau[self.x][self.y] = 'P'

    def droite(self):
        if self.x < self.taille_plateau - 1:
            self.plateau[self.x][self.y] = '.'
            self.x += 1
            self.plateau[self.x][self.y] = 'P'

    def haut(self):
        if self.y > 0:
            self.plateau[self.x][self.y] = '.'
            self.y -= 1
            self.plateau[self.x][self.y] = 'P'

    def bas(self):
        if self.y < self.taille_plateau - 1:
            self.plateau[self.x][self.y] = '.'
            self.y += 1
            self.plateau[self.x][self.y] = 'P'

    def position(self):
        return self.x, self.y

    def afficher_plateau(self):
        for ligne in self.plateau:
            print(" ".join(ligne))

personnage = Personnage()

print("Position initiale :", personnage.position())

personnage.droite()
personnage.bas()

print("Nouvelle position :", personnage.position())

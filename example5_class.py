class Rectangle:
    """classe des rectangles."""
    def __init__(self, longueur=0, largeur=0):
        "Initialisation avec valeurs par defaut"
        self.lon = longueur
        self.lar = largeur
        self.nom = "rectangle"
    def surface(self):
        "Retourne la surface d'un rectangle."
        return self.lon*self.lar
    def __str__(self):
        "Affichage des caracteristiques d'un rectangle."
        return ("\nLe {} de cotes {} et {} a une surface de {}".format(self.nom, self.lon, self.lar, self.surface()))


class Carre(Rectangle):
    """classe des carres (herite de Rectangle)."""
    def __init__(self, cote=0):
        "Constructeur avec valeur par defaut"
        Rectangle.__init__(self, cote, cote)
        self.nom = "carre" # surchage d'attribut d'instance

# Auto-test ---------------------------------------------------------
if __name__ == '__main__':
    r = Rectangle(12, 8)
    print(r)
    c = Carre(134)
    print(c)


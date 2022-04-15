class JeuDeCarte:

    def __init__(self):
        numero = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
        # Cœur carreau pique trèfle
        couleur = (1, 2, 3, 4)
        self.carte = []
        for couleur in couleur:
            for num in numero:
                self.carte.append((num, couleur))

    @staticmethod
    def nomCarte(carte: tuple):
        # On retourne le nom de la carte
        # Dictionnaire des noms de cartes
        superieur = {11: "Valet", 12: "Dame", 13: "Roi", 14: "As"}
        enseigne = {1: "Coeur", 2: "Carreau", 3: "Pique", 4: "Trèfle"}

        # Soit, elle est supérieure à 10 et on retourne son nom
        if carte[0] in superieur:
            return superieur[carte[0]] + " de " + enseigne[carte[1]]

        # soit, elle est inférieure à 10
        else:
            return str(carte[0]) + " de " + enseigne[carte[1]]

    def melanger(self):
        # On mélange les cartes
        import random
        random.shuffle(self.carte)
        return self.carte

    def tirer(self):
        # On retire la carte du dessus
        if not len(self.carte):
            return None
        else:
            return self.carte.pop(0)


if __name__ == "__main__":
    jeu = JeuDeCarte()
    jeu.melanger()

    for i in range(53):
        c = jeu.tirer()
        if c is not None:
            print(jeu.nomCarte(c))
        else:
            print("Pas de carte")

from jeuDeCarte import *


def getCarte(carte):
    a = JeuDeCarte()
    li = []
    for tup in carte:
        li.append(a.nomCarte(tup))
    return li


def getScore(carte):
    score = 0
    for tup in carte:
        if tup[0] == 14:
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        elif tup[0] > 10:
            score += 10
        else:
            score += tup[0]
    return score


def main(nbreJoueur=1):
    jeux = JeuDeCarte()
    jeux.melanger()

    # Boucle dans une liste à apprendre/améliorer.
    # On ajoute 1 pour le dealer.
    carte_joueur = [[1] for _ in range(nbreJoueur + 1)]
    for joueur in carte_joueur:
        joueur.append(jeux.tirer())
        joueur.append(jeux.tirer())

    # Commence par 1, le croupier étant le joueur 0.
    index_joueur_actuel = 1
    while True:
        if index_joueur_actuel > nbreJoueur:
            index_joueur_actuel = 1
            continue

        joueur_actuel = carte_joueur[index_joueur_actuel]

        # répétition... Comment faire mieux?
        liste_carte_croupier = getCarte(carte_joueur[0][1:])
        string_carte_croupier = ", ".join(liste_carte_croupier)
        liste_carte_actuelle = getCarte(joueur_actuel[1:])
        string_carte_actuelle = ", ".join(liste_carte_actuelle)

        # Condition si joueur toujours actif.
        if joueur_actuel[0] == 1:
            print(f"\nLe croupier possède: {string_carte_croupier}.\n")
            print(f"Au tour du joueur n°{index_joueur_actuel}")
            print(f"Vos cartes actuelles sont: {string_carte_actuelle}")

            while True:
                question = input("Voulez-vous tirer une carte? (o/n) ").lower()
                if question == "o":
                    joueur_actuel.append(jeux.tirer())
                    score = getScore(joueur_actuel[1:])
                    print(f"Vous avez eu {jeux.nomCarte(joueur_actuel[-1])}")
                    if score > 21:
                        print("Vous avez brulé.")
                        joueur_actuel[0] = 0
                        break
                else:
                    break

        index_joueur_actuel += 1


main(3)

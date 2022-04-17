from jeuDeCarte import *


def getCarte(carte):
    """
    Fonction qui retourne les cartes du joueur en texte.
    """
    a = JeuDeCarte()
    li = []
    for tup in carte:
        li.append(a.nomCarte(tup))
    return li


def getScore(carte):
    """
    Fonction qui calcule le score de carte que le joueux possède.
    """
    score = 0
    is_as = False
    for tup in carte:
        if tup[0] == 14:
            if score + 11 > 21:
                score += 1
            else:
                score += 11
                is_as = True
        elif tup[0] > 10:
            score += 10
        else:
            score += tup[0]

        if is_as:
            if score + tup[0] > 21:
                score -= 10
                is_as = False

    return score


def setup(nbreJoueur, jeux):
    """
    Fonction qui distribue les cartes à tout le monde en début de partie
    """

    # Boucle dans une liste à apprendre/améliorer.
    # index[0] pour le croupier.
    carte_joueur = [[1] for _ in range(nbreJoueur + 1)]
    for joueur in carte_joueur:
        joueur.append(jeux.tirer())
        joueur.append(jeux.tirer())
    return carte_joueur


def joueurDedans(liste):
    """
    Fonction qui vérifie si les joueurs sont dans la partie.
    """
    for joueur in liste:
        if joueur[0] == 1:
            return True
    return False


def main(nbreJoueur=1):
    jeux = JeuDeCarte()
    jeux.melanger()
    carte_joueur = setup(nbreJoueur, jeux)

    # Commence par 1, le croupier étant le joueur 0.
    index_joueur_actuel = 1
    while True:
        if index_joueur_actuel > nbreJoueur:
            index_joueur_actuel = 1
            continue
        if joueurDedans(carte_joueur):
            joueur_actuel = carte_joueur[index_joueur_actuel]

            # répétition... Comment faire mieux?
            liste_carte_croupier = getCarte(carte_joueur[0][1:])
            string_carte_croupier = ", ".join(liste_carte_croupier)
            liste_carte_actuelle = getCarte(joueur_actuel[1:])
            string_carte_actuelle = ", ".join(liste_carte_actuelle)

            # Condition si joueur toujours actif.
            if joueur_actuel[0] == 1:
                print(f"Le croupier possède: {string_carte_croupier}.\n")
                print(f"Au tour du joueur n°{index_joueur_actuel}")
                print(f"Vos cartes actuelles sont: {string_carte_actuelle}")

                # Demande action joueur.
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
                        joueur_actuel[0] = 0
                        break
                print()

            # Action croupier.
            if index_joueur_actuel == nbreJoueur:
                croupier_score = getScore(carte_joueur[0][1:])
                if 17 <= croupier_score <= 21:
                    print(f"Le croupier a eu {jeux.nomCarte(carte_joueur[0][-1])}")
                    carte_joueur[0][0] = 0
                else:
                    carte_joueur[0].append(jeux.tirer())
                    if getScore(carte_joueur[0][1:]) > 21:
                        print("Le croupier a brulé.")
                        break

            index_joueur_actuel += 1
        else:
            break

    # Affichage des résultats.
    print()
    croupier = getScore(carte_joueur[0][1:])
    for mec in carte_joueur[1:]:
        joueur = getScore(mec[1:])
        if joueur > 21:
            print(f"Le joueur n°{carte_joueur.index(mec)} a perdu!")
            continue
        if joueur > croupier or croupier > 21:
            print(f"Le joueur n°{carte_joueur.index(mec)} a gagné!")
        elif joueur < croupier:
            print(f"Le croupier a gagné sur le joueur n°{carte_joueur.index(mec)}.")
        else:
            print("Egalité.")


if __name__ == "__main__":
    main(3)

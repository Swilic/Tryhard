from Liste_de_mot import mot as m
import random


def main(vie=10):
    vie = vie
    mot = random.choice(m).upper()
    lettre_trouver = ""
    # Garde une trace si le mot est complet
    continuer = ""
    while vie > 0:

        # Print _ ou la lettre
        for i in range(len(mot)):
            # Si la lettre du mot est dans les trouvées print
            if mot[i] in lettre_trouver:

                # Recopie les lettres trouvées dans continuer pour avoir une condition de fin
                continuer += mot[i]
                print(mot[i], end=' ')
            else:
                continuer += "_"
                print("_", end=' ')
        print()

        # Fin du jeu si toutes lettres sont trouvés
        if continuer == mot:
            print("Vous avez gagné!")
            break
        else:
            continuer = ""

        ask = input("Choissisez une lettre: ").upper()

        # N'accepte que 1 lettre!
        if len(ask) > 1:
            print("Veuillez insérer que une lettre.")
        else:

            # Ajoute la lettre dans un mot si elle a pas été utilisée
            if not(ask in mot) and not(ask in lettre_trouver):
                vie -= 1
                print("Vous avez perdu une vie!")
            if not(ask in lettre_trouver):
                lettre_trouver += ask + " "
            print(f"Les lettres que vous avez essayées: {lettre_trouver}")
            print(f"Il vous reste {vie} vies.")


main()

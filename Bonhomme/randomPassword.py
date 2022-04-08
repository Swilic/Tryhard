import random
import string


def randomPassword(length):
    # Génération d'un mot de passe.
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits)

    # Chaque condition est de base fausse.
    lettre_maj = False
    lettre_min = False
    chiffre = False

    # Vérification des conditions du mot de passe
    for i in password:
        if i.isupper():
            lettre_maj = True
        if i.islower():
            lettre_min = True
        if i.isdigit():
            chiffre = True

    # Si aucune condition n'est respectée, on recommence
    if lettre_maj and lettre_min and chiffre:
        return password
    else:
        return randomPassword(length)


if __name__ == '__main__':
    print(randomPassword(10))

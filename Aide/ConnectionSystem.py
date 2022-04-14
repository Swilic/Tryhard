# Module pour masquer ce qui est écrit dans le terminal.
from stdiomask import getpass
# Module pour hasher le mot de passe.
import hashlib
# Module pour gérer les fichiers.
import os


# Fonction d'une ligne (lambda) pour nettoyer le terminal
def clear():
    os.system("cls")


def main():
    # Nettoie le terminal.
    clear()
    # Affiche l'écran d'accueil
    print("MAIN MENU")
    print("---------")
    print()
    print("1. Register")
    print("2. Login")
    print()
    # Tant que l'utilisateur n'a pas choisi une option, il reste dans la boucle.
    while True:
        print()
        user_choice = input("Choose An Option: ")
        if user_choice in ["1", "2"]:
            break

    # Lance la fonction que l'utilisateur a choisie.
    if user_choice == "1":
        register()
    else:
        login()


def register():
    clear()
    print("REGISTER")
    print("--------")
    print()

    # Demande le nom d'utilisateur.
    while True:
        user_name = input("Username: ").title()
        if user_name != "":
            break
    user_name = sanitize_name(user_name)

    # Demande le mot de passe.
    while True:
        # get pass et pas input, car on veut masquer le mot de passe.
        user_password = getpass()
        if user_password != "":
            break

    # Confirme le mot de passe.
    while True:
        confirme_password = getpass(prompt="Confirm password: ")
        if confirme_password == user_password:
            break
        else:
            print("Passwords don't match!")
            print()

    # Si le nom et le mot de passe sont libres.
    if user_already_exist(user_name, user_password):
        while True:
            print()
            error = input("User already exist!\n\n Press (T) To try again\n Press (L) To login: ").lower()
            if error == "t":
                return register()
            elif error == "l":
                return login()
    add_user_info([user_name, hash_password(user_password)])

    print()
    print("User successfully registered!")


def login():
    clear()
    print("LOGIN")
    print("-----")
    print()
    user_info = {}

    with open("users.txt", "r") as file:
        # Lit ligne par ligne.
        for line in file:
            line = line.split()
            user_info.update({line[0]: line[1]})

    # Demande le nom d'utilisateur.
    while True:
        user_name = input("Username: ").title()
        user_name = sanitize_name(user_name)
        if user_name not in user_info:
            print("User doesn't exist!")
            print()
        else:
            break

    # Demande le mot de passe. Tant que le mot de passe n'est pas correct, on continue.
    while True:
        user_password = getpass(prompt="Password: ")
        if not check_password_hash(user_password, user_info[user_name]):
            print("Wrong password!")
            print()
        else:
            break

    print("User successfully logged in!")


# Fonction pour ajouter les informations de l'utilisateur dans le fichier.
# Prend comme argument une liste.
def add_user_info(userinfo: list):
    with open("users.txt", "a") as file:
        file.write(userinfo[0] + " " + userinfo[1] + "\n")


def user_already_exist(user_name, user_password):
    with open("users.txt", "r") as file:
        for line in file:
            line = line.split()
            # Si le nom d'utilisateur existe déjà.
            # On prend le mot de passe de l'utilisateur qui provient du fichier --> Donc hashé.
            if line[0] == user_name and line[1] == hash_password(user_password):
                return True
    return False


def sanitize_name(user_name):
    return user_name.replace(" ", "-")


def hash_password(password):
    # Chiffre le mot de passe.
    return hashlib.sha256(password.encode()).hexdigest()


def check_password_hash(password, hach):
    # Vérifie si le mot de passe correspond à la hash.
    return hash_password(password) == hach


main()

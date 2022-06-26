from classQuiz import Quiz


def main():
    # Initialise le fichier de questions
    joueur = Quiz("D:/Coding/Tryhard/questionCapitalPays.txt")

    choice = input("Voulez-vous jouer avec de l'aide? o/n")
    if choice == "o":
        qcm(joueur)
    else:
        normal(joueur)

    # Affiche le score
    print(f"Vous avez {joueur.score}/5")

    # Propose de jouer à nouveau
    again = input("Voulez-vous faire un autre quizz ? (o/n) ")
    if again == "o":
        main()


def question(joueur):
    # Choisi, demande et vérifie.
    joueur.getQuestion()


def validation(joueur):
    essai = input("Votre réponse? ")
    joueur.checkAnswer(essai)


def normal(joueur):
    
    # 5 questions au total
    for i in range(5):
        question(joueur)
        validation(joueur)


def qcm(joueur):
    # Lance le QCM
    for i in range(5):
        question(joueur)

        lesChoix = joueur.choixmultiple()
        for j in range(4):
            print(lesChoix[j])
        print()

        validation(joueur)


main()

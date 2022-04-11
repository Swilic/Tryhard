from classQuiz import Quiz


def main():
    # Initialise le fichier de questions
    moi = Quiz("D:/Coding/Tryhard/questionCapitalPays.txt")

    # 5 questions au total
    for i in range(5):
        # Choisi, demande et vérifie.
        moi.getQuestion()
        reponse = input("Votre réponse? ")
        moi.checkAnswer(reponse)
        print()

    # Affiche le score
    print(f"Vous avez {moi.score}/5")

    # Propose de jouer à nouveau
    again = input("Voulez-vous faire un autre quizz ? (o/n) ")
    if again == "o":
        main()


main()

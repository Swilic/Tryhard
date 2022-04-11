import random


class Quiz:
    def __init__(self, filename):
        self.question = []
        self.answer = []
        self.score = 0
        self.currentQuestion = []

        # Ouvre le fichier, le parcours ligne par ligne et ajoute les questions et les réponses dans les listes
        with open(filename, "r", encoding="utf-8") as f:
            for lie in f.read().splitlines():
                self.question.append(lie.split(" - ")[0])
                self.answer.append(lie.split(" - ")[1])

    def getQuestion(self):
        # Choisit une question au hasard dans la liste
        x = random.randint(0, len(self.question))

        # Vérifie qu'elle n'a pas déjà été posée
        if x in self.currentQuestion:
            return self.getQuestion()
        else:
            self.currentQuestion.append(x)
            print(f"Quelle est la capitale de {self.question[x]}? ")

    def getAnswer(self):
        return self.answer[self.currentQuestion[-1]]

    def checkAnswer(self, answer):
        if answer.lower() == self.getAnswer().lower():
            self.score += 1

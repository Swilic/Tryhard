import random


class Quiz:
    def __init__(self, filename):
        self.question = []
        self.answer = []
        self.score = 0
        self.currentQuestion = []

        # Ouvre le fichier, le parcours ligne par ligne et ajoute les questions et les réponses dans les listes
        with open(filename, "r", encoding="utf-8") as f:
            for element in f.read().splitlines():
                self.question.append(element.split(" - ")[0])
                self.answer.append(element.split(" - ")[1])

    def getQuestion(self):
        # Choisit une question au hasard dans la liste avec l'index
        land = random.randint(0, len(self.question))

        # Vérifie qu'elle n'a pas déjà été posée
        if land in self.currentQuestion:
            return self.getQuestion()
        else:
            self.currentQuestion.append(land)
            print(f"Quelle est la capitale de {self.question[land]}? ")

    def getAnswer(self):
        return self.answer[self.currentQuestion[-1]]

    def checkAnswer(self, answer):
        if answer.lower() == self.getAnswer().lower():
            self.score += 1

    def choixmultiple(self):
        qcm = [self.answer[self.currentQuestion[-1]]]

        # Ajoute la réponse de la question dans la liste
        for i in range(3):
            fausse = random.choice(self.answer)
            while fausse in qcm:
                fausse = random.choice(self.answer)
            qcm.append(fausse)

        random.shuffle(qcm)
        return qcm


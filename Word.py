import random


class Word:

    def __init__(self):
        words = Word.load_words().split(' ')
        integer = random.randrange(0, len(words) - 1)
        self.mot_a_deviner = words[integer]
        del words
        self.longueur = len(self.mot_a_deviner)
        self.mot_cache = None
        self.trials = 8

    @staticmethod
    def load_words() -> str:
        with open("mots8Lettres.txt", "r", encoding='utf8') as fileScores:
            return fileScores.read()

    def creationMotCache(self):
        mot = []
        i = 0
        while i < self.longueur:
            mot.append("*")
            i += 1
        self.mot_cache = mot
        return mot

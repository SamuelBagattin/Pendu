import random

import variables


class Word:

    def __init__(self):
        nombreLettres = random.randrange(1, 8)
        motChiffres = []

        # construction aléatoire du mot
        i = 0
        while i <= nombreLettres:
            motChiffres.append(random.randrange(1, 26))
            i += 1

        self.mot_a_deviner = Word.mot_en_lettre(motChiffres)
        self.longueur = len(self.mot_a_deviner)
        self.mot_cache = None
        self.trials = 8

    @staticmethod
    def mot_en_lettre(mot_chiffres: list):
        liste = []
        for elt in mot_chiffres:
            liste.append(variables.alphabet[elt - 1])
        return liste

    def creationMotCache(self):
        mot = []
        i = 0
        while i < self.longueur:
            mot.append("*")
            i += 1
        self.mot_cache = mot
        return mot

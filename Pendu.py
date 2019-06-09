import os
import pickle

import variables
from Word import Word


class Pendu:
    CONTINUE_GAME = "o"

    MENU_SCORES = "2"
    MENU_GAME = "1"
    MENU_EXIT = "3"

    MENU_CHOICES = [MENU_GAME, MENU_SCORES, MENU_EXIT]

    def __init__(self):
        self.word = None
        self.username = None
        self.scores = None
        self.letter_input = None
        self.choice_menu = 0
        self.choice_continue = "o"

    def init_word(self) -> None:
        self.word = Word()
        self.word.creationMotCache()

    def load_scores(self) -> None:
        def load():
            with open("scores", "rb") as file:
                unpickler = pickle.Unpickler(file)
                self.scores = dict(unpickler.load())

        try:
            load()
        except FileNotFoundError:
            with open("scores", "wb+") as fileScores:
                pickler = pickle.Pickler(fileScores)
                pickler.dump({})
            self.scores = None

    def prompt_menu(self) -> None:
        print("Choisissez une option : ")
        print("1 : jouer au pendu")
        print("2 : afficher le tableau des scores")
        print("3 : quitter")
        self.choice_menu = input()

    def prompt_scores(self) -> None:
        Pendu.cls()
        if self.scores:
            print("Voici le tableau des scores : ")
            for username, score in self.scores.items():
                print(f'{username} : {score}')
        else:
            print('Aucun score enregistré pour l\'instant')
        print('\n')

    def prompt_hidden_word(self) -> None:
        print("".join(self.word.mot_cache))

    def prompt_and_set_username(self) -> None:
        self.username = input("Votre nom : ")

    def test_word_found(self) -> bool:
        return self.word.mot_a_deviner == "".join(self.word.mot_cache)

    def prompt_and_control_letter_input(self) -> None:
        try:
            self.letter_input = input("Entrez une lettre : ")
            assert variables.alphabet.count(self.letter_input.upper()) == 1
        except AssertionError:
            while variables.alphabet.count(self.letter_input.upper()) != 1:
                self.letter_input = input("Entrez une lettre et une seule ! : ")

    def add_letter(self) -> None:
        for i, elt in enumerate(self.word.mot_a_deviner):
            if elt == self.letter_input.upper():
                self.word.mot_cache[i] = self.letter_input.upper()

    def prompt_lose(self) -> None:
        print("Vous avez perdu\nLe pendu.mot etait :")
        print("".join(self.word.mot_a_deviner))

    def prompt_win(self) -> None:
        print("Vous avez gagne")

    def record_scores(self) -> None:
        if self.username in self.scores:
            self.scores[self.username] += self.word.trials
        else:
            self.scores[self.username] = self.word.trials
        with open("scores", "wb") as fileScores:
            pickler = pickle.Pickler(fileScores)
            pickler.dump(self.scores)

    @staticmethod
    def cls() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

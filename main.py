# -*-coding:UTF-8 -*-
from Pendu import Pendu

pendu = Pendu()
pendu.load_scores()

# menu
while pendu.choice_continue == Pendu.CONTINUE_GAME or pendu.choice_menu in Pendu.MENU_CHOICES:
    pendu.prompt_menu()

    if pendu.choice_menu == Pendu.MENU_SCORES:
        pendu.prompt_scores()

    if pendu.choice_menu == Pendu.MENU_GAME:
        Pendu.cls()
        pendu.init_word()

        pendu.prompt_hidden_word()
        print("".join(pendu.word.mot_a_deviner))

        pendu.prompt_and_set_username()

        while not pendu.test_word_found():
            pendu.prompt_and_control_letter_input()
            pendu.add_letter()
            Pendu.cls()
            pendu.prompt_hidden_word()
            if pendu.word.trials == 0:
                pendu.prompt_lose()
                break
            pendu.word.trials -= 1

        if pendu.test_word_found():
            pendu.record_scores()
            pendu.prompt_win()

    if pendu.choice_menu == Pendu.MENU_EXIT:
        Pendu.cls()
        exit()

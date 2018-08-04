# -*-coding:UTF-8 -*-
import os
import random
import math
import fonctions
import variables
import pickle

with open("scores", "rb") as fileScores:
    unpickler = pickle.Unpickler(fileScores)
    scores = unpickler.load()

choix = "o"

#menu
while choix == "o" or choixOption in ["1", "2", "3"]:
    print("Choisissez une option : ")
    print("1 : jouer au pendu")
    print("2 : afficher le tableau des scores")
    print("3 : quitter")
    choixOption = input()

    if choixOption == "2":
        fonctions.cls()
        print("Voici le tableau des scores : ")
        print(scores)
        print("")

    if choixOption == "1":
        fonctions.cls()
        nombreLettres = random.randrange(1, 8)
        trials = 8
        motChiffres = []

        #construction aléatoire du mot
        i = 0
        while i<=nombreLettres:
            motChiffres.append(random.randrange(1,26))
            i+=1

        motADeviner = fonctions.motEnLettres(motChiffres)

        #construction du mot caché
        motDevine = fonctions.creationMotCache(nombreLettres+1)
        print("".join(motDevine))
        print("".join(motADeviner))

        #nom de l'utilisateur
        nomUtilisateur = input("Votre nom : ")

        #jeu du pendu
        while motADeviner != motDevine:
            try:
                inputLettre = input("Entrez une lettre : ")
                assert variables.alphabet.count(inputLettre) == 1
            except AssertionError:
                inputLettre = input("Entrez une lettre et une seule ! : ")
                while variables.alphabet.count(inputLettre) != 1:
                   inputLettre = input("Entrez une lettre et une seule ! : ")

            motDeviner = fonctions.ajoutLettres(motDevine, motADeviner, inputLettre)
            fonctions.cls()
            print("".join(motDevine))
            trials-=1

            if motADeviner == motDevine:
                print("Vous avez gagne")
            if trials == 0:
                print("Vous avez perdu \nLe mot etait :")
                print("".join(motADeviner))
                break

        #enregistrement du score
        if nomUtilisateur in scores:
            scores[nomUtilisateur] += trials
        else:
            scores[nomUtilisateur] = trials
        with open("scores", "wb") as fileScores:
            pickler = pickle.Pickler(fileScores)
            pickler.dump(scores)

    if choixOption == "3":
        fonctions.cls()
        exit()
        


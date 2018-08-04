# -*-coding:UTF-8 -*-
import os
import random
import math
import variables

#conversion d'un chiffre en lettre
def chiffreEnLettre(num):
    result = variables.alphabet[num-1]
    return result

#conversion d'une liste de chiffre en liste de lettres
def motEnLettres(mot):
    list=[]
    for elt in mot:
        list.append(chiffreEnLettre(elt))
    return list

#création de la liste cachée en fonction du nombre d'elements dans la liste de lettres
def creationMotCache(taille):
    mot = []
    i=0
    while i<taille:
        mot.append("*")
        i+=1
    return mot

#ajout des lettres dans le mot
def ajoutLettres(listeCachee, listeADecouvrir, inputUtilisateur):
    for i, elt in enumerate(listeADecouvrir):
        if elt == inputUtilisateur :
           listeCachee[i] = inputUtilisateur
    return listeCachee

#clear screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
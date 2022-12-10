#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:16:46 2022

@author: mathieuthibaud
"""

"""
donnees = [
'1000',
'2000',
'3000',
"",
'4000',
"",
'5000',
'6000',
"",
'7000',
'8000',
'9000',
"",
'10000',
]
"""

fichier = open("input.txt", "r")

donnees = fichier.read().splitlines()


donnees.append("")

def partie1(liste):
    listessommes = []
    somme = 0
    for i in range(len(liste)):
        if liste[i] == "":
            listessommes.append(somme)
            somme = 0
        else:
            somme += int(liste[i])
    return max(listessommes)


def partie2(liste):
    listessommes = []
    somme = 0
    for i in range(len(liste)):
        if liste[i] == "":
            listessommes.append(somme)
            somme = 0
        else:
            somme += int(liste[i])
    listessommes.sort()
    return sum(listessommes[-3:])



print("Advent Of Code 2022")
print("Jour 1")
print("Partie 1 :")
print(f"La réponse est : {partie1(donnees)}")
print("Partie 2 :")
print(f"La réponse est : {partie2(donnees)}")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:16:46 2022

@author: mathieuthibaud
"""



fichier = open("input", "r")

donnees = fichier.read().splitlines()

"""

donnees = ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw',]
"""


def rechercheele(sac):
    for ele in sac[:len(sac)//2]:
        for ele2 in sac[len(sac)//2:]:
            if ele == ele2:
                return ele



def partie1(liste):
    resultat = 0
    for ligne in liste:
        lettre = rechercheele(ligne)
        if ord(lettre)>=97:
            resultat +=  ord(lettre) - 96
        else:
            resultat += ord(lettre) - 64 +26
    return resultat

def recherchebadge(trio):
    for ele in trio[0]:
        if ele in trio[1] and ele in trio[2]:
            return ele

def partie2(liste):
    resultat = 0
    for i in range(len(liste)//3):
        badge = recherchebadge(liste[3*i:3*(i+1)])
        if ord(badge) >= 97:
            resultat +=  ord(badge) - 96
        else:
            resultat += ord(badge) - 64 +26
    return resultat                     



print("Advent Of Code 2022")
print("Jour 3")
print("Partie 1 :")
print(f"La réponse est : {partie1(donnees)}")
print("Partie 2 :")
print(f"La réponse est : {partie2(donnees)}")



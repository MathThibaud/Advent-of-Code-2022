#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:16:46 2022

@author: mathieuthibaud
"""



fichier = open("input", "r")

donnees = fichier.read().splitlines()
"""
donnees = ['A Y', 'B X', 'C Z']
"""
dic = {"X" : 1, "Y": 2, "Z" : 3, "A" : 1, "B" : 2, 'C' : 3}

def tour1(ordi, moi):
    if dic[ordi] == dic[moi]:
        return 3 + dic[moi]
    if (ordi == "A" and  moi == "Y") or (ordi == "B" and moi == 'Z') or (ordi == 'C' and moi == "X"):
        return 6 + dic[moi]
    else:
        return dic[moi]


def jeu1(liste):
    score = 0
    for ele in liste:
        score += tour1(ele[0], ele[-1])
    return score


def tour2(ordi, result):
    if result == 'X':
        if ordi == 'A':
            return 3
        elif ordi == "B":
            return 1
        else:
            return 2
    if result == "Y":
        return 3 + dic[ordi]
    else:
        if ordi == "A":
            return 8
        elif ordi == "B":
            return 9
        else:
            return 7
    
def jeu2(liste):
    score = 0
    for ele in liste:
        score += tour2(ele[0], ele[-1])
    return score
    


print("Advent Of Code 2022")
print("Jour 2")
print("Partie 1 :")
print(f"La réponse est : {jeu1(donnees)}")
print("Partie 2 :")
print(f"La réponse est : {jeu2(donnees)}")



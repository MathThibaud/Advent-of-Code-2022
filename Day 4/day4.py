#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:16:46 2022

@author: mathieuthibaud
"""



fichier = open("input", "r")

donnees = fichier.read().splitlines()


"""
donnees = ['2-4, 6-8',
'2-3,4-5',
'5-7,7-9',
'2-8,3-7',
'6-6,4-6',
'2-6,4-8']
"""

def traitement1(liste):
    resultat = []
    for ele in liste:
        i = 0
        while i < len(ele):
            if ele[i] == ',':
                resultat.append([ele[:i], ele[i+1:]])
            i += 1
    return resultat

def traitement2(liste):
    resultat = []
    for ele in liste:
        i = 0
        while i < len(ele):
            if ele[i] == '-':
                resultat.append([int(ele[:i]), int(ele[i+1:])])
            i += 1
    return resultat
 
donnees = traitement1(donnees)  
new = [] 
for ele in donnees:
    ele = traitement2(ele)
    new.append(ele)
    
    
def partie1(liste):
    resultat = 0
    for ele in liste:
        if ele[0][0] <= ele[1][0] and ele[1][1] <= ele[0][1]:
            resultat += 1
        elif ele[1][0] <= ele[0][0] and ele[0][1] <= ele[1][1]:
            resultat += 1
    return resultat
            


def partie2(liste):
    resultat = len(liste)
    for ele in liste:
        if ele[0][1] < ele[1][0] or ele[1][1] < ele[0][0]:
            resultat -= 1
    return resultat
            
        



print("Advent Of Code 2022")
print("Jour 4")
print("Partie 1 :")
print(f"La réponse est : {partie1(new)}")
print("Partie 2 :")
print(f"La réponse est : {partie2(new)}")



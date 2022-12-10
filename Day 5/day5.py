#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:16:46 2022

@author: mathieuthibaud
"""



fichier = open("input", "r")

donnees = fichier.read().splitlines()


CAISSES = donnees[:donnees.index("")]


# Partie 1

"""
P1 = [CAISSES[i][1] for i in range((len(CAISSES))-2, -1, -1)]
P2 = [CAISSES[i][5] for i in range((len(CAISSES))-2, -1, -1)]
P3 = [CAISSES[i][9] for i in range((len(CAISSES))-2, -1, -1)]
P4 = [CAISSES[i][13] for i in range((len(CAISSES))-2, -1, -1)]
P5 = [CAISSES[i][17] for i in range((len(CAISSES))-2, -1, -1)]
P6 = [CAISSES[i][21] for i in range((len(CAISSES))-2, -1, -1)]
P7 = [CAISSES[i][25] for i in range((len(CAISSES))-2, -1, -1)]
P8 = [CAISSES[i][29] for i in range((len(CAISSES))-2, -1, -1)]
P9 = [CAISSES[i][33] for i in range((len(CAISSES))-2, -1, -1)]


caisses = [P1, P2, P3, P4, P5, P6, P7, P8, P9]
"""


caisses = [[CAISSES[i][1+4*k] for i in range((len(CAISSES))-2, -1, -1)] for k in range(9)]


for ligne in caisses:
    while ligne[-1] == ' ':
        ligne.pop()
        
caisses = [""] + caisses  # Uniquement là pour faciliter indicage



MOUVS = donnees[donnees.index("")+1:]

long = [len(ligne) for ligne in MOUVS]

mouvs = []
for ligne in MOUVS:
    if len(ligne) == 18:
        ajout = [int(ligne[5]), int(ligne[12]), int(ligne[17])]
        mouvs.append(ajout)
    else:
        ajout = [int(ligne[5:7]), int(ligne[13]), int(ligne[18])]
        mouvs.append(ajout)



for ligne in mouvs:
    annexe = []
    for _ in range(ligne[0]):
        a = caisses[ligne[1]].pop()
        caisses[ligne[2]].append(a)


mot = [caisses[i][-1] for i in range(1, len(caisses))]

resultat1 = ""
for ele in mot:
    resultat1 += ele

#partie 2

"""
P1 = [CAISSES[i][1] for i in range((len(CAISSES))-2, -1, -1)]
P2 = [CAISSES[i][5] for i in range((len(CAISSES))-2, -1, -1)]
P3 = [CAISSES[i][9] for i in range((len(CAISSES))-2, -1, -1)]
P4 = [CAISSES[i][13] for i in range((len(CAISSES))-2, -1, -1)]
P5 = [CAISSES[i][17] for i in range((len(CAISSES))-2, -1, -1)]
P6 = [CAISSES[i][21] for i in range((len(CAISSES))-2, -1, -1)]
P7 = [CAISSES[i][25] for i in range((len(CAISSES))-2, -1, -1)]
P8 = [CAISSES[i][29] for i in range((len(CAISSES))-2, -1, -1)]
P9 = [CAISSES[i][33] for i in range((len(CAISSES))-2, -1, -1)]


caisses2 = [P1, P2, P3, P4, P5, P6, P7, P8, P9]
"""
caisses2 = [[CAISSES[i][1+4*k] for i in range((len(CAISSES))-2, -1, -1)] for k in range(9)]

for ligne in caisses2:
    while ligne[-1] == ' ':
        ligne.pop()
        
caisses2 = [""] + caisses2  # Uniquement là pour faciliter indicage

for ligne in mouvs:
    annexe = []
    for _ in range(ligne[0]):
        a = caisses2[ligne[1]].pop()
        annexe.append(a)
    while len(annexe) != 0:
        a = annexe.pop()
        caisses2[ligne[2]].append(a)



mot = [caisses2[i][-1] for i in range(1, len(caisses2))]

resultat2 = ""
for ele in mot:
    resultat2 += ele


print("Advent Of Code 2022")
print("Jour 5")
print("Partie 1 :")
print(f"La réponse est : {resultat1}")
print("Partie 2 :")
print(f"La réponse est : {resultat2}")


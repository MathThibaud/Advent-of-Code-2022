#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:31:30 2022

@author: mathieuthibaud
"""

fichier = open("input", "r")

donnees = fichier.read().splitlines()


CAISSES = donnees[:9]

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

for ligne in caisses:
    while ligne[-1] == ' ':
        ligne.pop()
        
caisses = [""] + caisses

MOUVS = donnees[10:]

long = [len(ligne) for ligne in MOUVS]

mouvs = []
for ligne in MOUVS:
    if len(ligne) == 18:
        ajout = [int(ligne[5]), int(ligne[12]), int(ligne[17])]
        mouvs.append(ajout)
    else:
        ajout = [int(ligne[5:7]), int(ligne[13]), int(ligne[18])]
        mouvs.append(ajout)
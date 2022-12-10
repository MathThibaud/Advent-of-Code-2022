#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:16:46 2022

@author: mathieuthibaud
"""


"""
fichier = open("inputassert", "r")
"""
fichier = open("input", "r")

donnees = fichier.read().splitlines()

for i in range(len(donnees)):
    donnees[i] = donnees[i].split(" ")
    
    
  
def sequences(donnees):
    c = 1
    x = 1
    liste = [(0,0), (c, x)]
    for ligne in donnees:
        if ligne[0] == 'noop':
            c = c+1
            new = (c, x)
            liste.append(new)
        else:
            c += 1
            new = (c, x)
            liste.append(new)
            c += 1
            x += int(ligne[1])
            new = (c, x)
            liste.append(new)
    return liste

def partie1(liste):
    somme = 0
    for i in range(6):
        somme += liste[20+40*i][1] * (20+40*i)
    return somme
    

def position(ligne):
    return ligne[1], ligne[1]+1, ligne[1]+2

def partie2(liste):
    total = ""
    for j in range(6):
        ligne = ""
        for i in range(1, 40):
            if liste[i+40*j][0]%40 == liste[i+40*j][1] or liste[i+40*j][0]%40 == liste[i+40*j][1]+1 or liste[i+40*j][0]%40 == liste[i+40*j][1] + 2:
                ligne += "#"
            else:
                ligne += " "
        ligne += "\n"
        total += ligne
    print(total)
    
                
        
print("Advent Of Code 2022")
print("Jour 10")
print("Partie 1 :")
print(f"La réponse est : {partie1(sequences(donnees))}")
print("Partie 2 :")
print("La réponse est :")
partie2(sequences(donnees))



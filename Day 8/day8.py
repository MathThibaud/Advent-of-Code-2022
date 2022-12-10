#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:16:46 2022

@author: mathieuthibaud
"""



fichier = open("input", "r")

donnees = fichier.read().splitlines()


"""

donnees = ['30373',
'25512',
'65332',
'33549',
'35390']
"""

n = len(donnees)





def visible_h(i, j):
    for k in range(i):
        if int(donnees[k][j]) >= int(donnees[i][j]):
            return False
    return True

def visible_b(i, j):
    for k in range(n-1, i, -1):
        if int(donnees[k][j]) >= int(donnees[i][j]):
            return False
    return True

def visible_g(i, j):
    for k in range(j):
        if int(donnees[i][k]) >= int(donnees[i][j]):
            return False
    return True

def visible_d(i, j):
    for k in range(n-1, j, -1):
        if int(donnees[i][k]) >= int(donnees[i][j]):
            return False
    return True
        

def est_visible(i, j):
    return visible_h(i, j) or visible_b(i, j) or visible_g(i, j) or visible_d(i, j)

def nouvelle_carte(donnees):
    carte = [[True for j in range(n)] for i in range(n)]
    for i in range(1,n-1):
        for j in range(1, n-1):
            carte[i][j] = est_visible(i, j)
    return carte

def partie1(donnees):
    return sum(sum(nouvelle_carte(donnees)[i]) for i in range(n))
    



def vision_h(i, j):
    k = 1
    while i-k> 0 and donnees[i-k][j] < donnees[i][j]:
        k += 1
    return k

def vision_b(i, j):
    k = 1
    while i+k< n-1 and donnees[i+k][j] < donnees[i][j]:
        k += 1
    return k

def vision_d(i, j):
   k = 1
   while j+k< n-1 and donnees[i][j+k] < donnees[i][j]:
       k += 1
   return k

def vision_g(i, j):
    k = 1
    while j-k > 0 and donnees[i][j-k] < donnees[i][j]:
        k += 1
    return k
        

def vision(i, j):
    return vision_h(i,j)*vision_b(i,j)*vision_g(i,j)*vision_d(i,j)


def nouvelles_carte_2(donnees):
    carte = [[vision(i, j) for j in range(n)] for i in range(n)]
    for i in range(n):
        carte[i][0] = 0
        carte[i][n-1] = 0
    for j in range(n):
        carte[0][j] = 0
        carte[n-1][j] = 0
    return carte
    
def partie2(donnees):
    return max(max(nouvelles_carte_2(donnees)[i]) for i in range(n))
    


print("Advent Of Code 2022")
print("Jour 8")
print("Partie 1 :")
print(f"La réponse est : {partie1(donnees)}")
print("Partie 2 :")
print(f"La réponse est : {partie2(donnees)}")



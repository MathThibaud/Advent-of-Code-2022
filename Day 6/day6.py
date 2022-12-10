#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:16:46 2022

@author: mathieuthibaud
"""



fichier = open("input", "r")

donnees = fichier.read()[:-1]


"""
donnees = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb',
           'bvwbjplbgvbhsrlpgdmjqwftvncz',
           'nppdvjthqldpwncqszvftbrmjlhg',
           'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
           'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
"""

def test(mot):
    for i in range(len(mot)):
        if mot.count(mot[i]) != 1:
            return False
    return True
        
        

def partie1(mot):
    for i in range(len(mot)-4):
        if test(mot[i: i+4]):
            return i +4
    return "fin"
        
def partie2(mot):
    for i in range(len(mot)-14):
        if test(mot[i: i+14]):
            return i + 14
    return "fin"    
   



print("Advent Of Code 2022")
print("Jour 6")
print("Partie 1 :")
print(f"La réponse est : {partie1(donnees)}")
print("Partie 2 :")
print(f"La réponse est : {partie2(donnees)}")



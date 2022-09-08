# python2C-unsam2022
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 01:18:51 2022

@author: datascience
"""
import random

def tirar(n):
    tirada=[]
    for i in range(n):
        tirada.append(random.randint(1,6)) 
    return tirada

tirar(3)
def es_generala(tirada):
    return tirada[0]==tirada[1]==tirada[2]==tirada[3]==tirada[4]




#guardar los datos que mas se repiten
def prob_generala():
    tirada=1
    dados=5
    juego=tirar(dados)
    print(juego[0])

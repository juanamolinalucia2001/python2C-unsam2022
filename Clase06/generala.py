# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:38:59 2022

@author: juani
"""

import random

def tirar(n):
    tirada=[] 
    for i in range(n): 
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    return tirada[0]==tirada[1]==tirada[2]==tirada[3]==tirada[4]

#guardar los datos que mas se repiten 
def prob_generala(tiros):
    while tiros>0:
        dados=5
        generala=[]
        juego= repetidos(tirar(dados))
        cara=max(juego, key=juego.get)
        veces_repeat=juego[select_cara]
        if veces_repeat>=2:
            generala.append(cara)
            dados=dados-veces_repeat
            
#veo mas repetido de la tirada {5: 1, 4: 2, 1: 2}
def repetidos(lista):
    repe={}
    for n in lista:
        if n in repe:
            repe[n]+=1
        else:
            repe[n]=1
        
    return repe


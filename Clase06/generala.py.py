# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:54:23 2022

@author: juani
"""
import random

def tirar(n):
    tirada=[] 
    for i in range(n): 
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    return len(tirada) == 5 and tirada[0]==tirada[1]==tirada[2]==tirada[3]==tirada[4]



def prob_generala():
    # tiro dados 1 vez
    caras = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    dados=5
    tirada=3
    juego1 = tirar(dados)
    

    #agrupo y veo qué salió
    for dado in juego1:
        caras[dado].append(dado)


    #selecciona cara si hay mas de 2 dados iguales
    dados_selec = []
    for num in caras:
       if len(caras[num]) >= 2 :
           dados_selec = caras[num]
   
    
    dados=5-len(dados_selec)
    tirada-=1
    while tirada>0:
        juego=tirar(dados)
        for i in juego:
            if i in dados_selec:
                dados_selec.append(i) 
        dados=5-len(dados_selec)
        tirada-=1
        
        print(tirada,dados,dados_selec)
        return es_generala(dados_selec)

N = 10000
G = sum([prob_generala() for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
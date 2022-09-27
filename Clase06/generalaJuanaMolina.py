# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:19:50 2022

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

def repetidos(lista):
    repe={}
    for n in lista:
        if n in repe:
            repe[n]+=1
        else:
            repe[n]=1
        
    return repe

def nueva_tirada(tirada_anterior):
    datos_tirada = repetidos(tirada_anterior)
    cara_max = max(datos_tirada, key=datos_tirada.get)
    cant_max = datos_tirada[cara_max]
    
    nueva_tirada = tirar(5 - cant_max)
    nueva_tirada += [cara_max] * cant_max
    
    return nueva_tirada

def generala_en_tres():
    # tiro dados 1 vez
    primera_tirada = tirar(5)
    #chequeo 
    if es_generala(primera_tirada):
        return True
    segunda_tirada=nueva_tirada(primera_tirada)
    if es_generala(segunda_tirada):
        return True
    tercer_tirada=nueva_tirada(segunda_tirada)
    if es_generala(tercer_tirada):
        return True
    return False
                               
N = 10000
G = sum([generala_en_tres() for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala en tres tiros o menos.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
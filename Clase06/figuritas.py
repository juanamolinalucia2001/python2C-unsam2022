#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:51:56 2022

@author: datascience
"""

import numpy as np
import random
import matplotlib.pyplot as plt

#figuritas
#DATOS
#Álbum con 670 figuritas.
#Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
#Cada paquete tiene cinco figuritas.

#Ejercicio 6.13: Crear
def crear_album(figus_total):
    album=np.zeros(figus_total,dtype=(int))
    return album


#Ejercicio 6.14: Incompleto
def album_incompleto(A):
    if 0 in A:
        return True
    else:
        return False

#A=[1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

#Ejercicio 6.15: Comprar
def comprar_figu(figus_total):
      return random.choice(np.arange(0, figus_total))

#Ejercicio 6.16: Cantidad de compras

def cuantas_figus(figus_total):
    album=crear_album(figus_total)
    cant_figus=0

    while album_incompleto(album):
        comprar=comprar_figu(figus_total)
        if(album[comprar]==0):
            album[comprar] += 1
        cant_figus+=1

    return cant_figus

#Ejercicio 6.17:
n_repeticiones = 1000
repeticiones = []
repeticiones.append([cuantas_figus(6) for i in range(n_repeticiones)])

prom_album_6 = np.mean(repeticiones)
print(prom_album_6)
#6.18
def experimento_figus(n_repeticiones, figus_total):
    lista= []
    lista.append([cuantas_figus(figus_total) for i in range(n_repeticiones)])
    prom_album = np.mean(lista)
   # return prom_album, lista
    return len(lista)/5
    
#6.19
#tiene 5 figus
def paquete_c(figus_total,figus_paquete):
    figus=[]
    while  len(figus)<figus_paquete:
        figu=random.choice(np.arange(0, figus_total))
        figus.append(figu)
    return figus

def comprar_paquete(figus_total, figus_paquete):
    paquete = np.random.choice(np.arange(0, figus_total), figus_paquete)
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    album=crear_album(figus_total)
    cant_figus=0
    paquetes=0
    while album_incompleto(album):
        comprar= comprar_paquete(figus_total, figus_paquete)
        album[comprar] += 1
        cant_figus+=figus_paquete
        paquetes+=1
    return paquetes
#6.2?
n_repeticiones = 100
repe= []
repe.append([cuantos_paquetes(670, 5) for i in range(n_repeticiones)])

prom_album = np.mean(repe)
print(prom_album)
#6.22
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = paquete_c(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

# figus_total = 670
# figus_paquete = 5
# plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
# plt.xlabel("Cantidad de paquetes comprados.")
# plt.ylabel("Cantidad de figuritas pegadas.")
# plt.title("La curva de llenado se desacelera al final")
# plt.show()

#6.23
n_repeticiones = 1000

cant=0
repe=[cuantos_paquetes(670, 5) for i in range(n_repeticiones)]
for e in repe:
    if e <= 850:
        cant+=1
print(cant/n_repeticiones)



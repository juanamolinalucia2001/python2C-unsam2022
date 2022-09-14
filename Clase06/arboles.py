# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:27:48 2022

@author: juani
"""

import numpy as np
import os
import matplotlib.pyplot as plt
import csv

def leer_arboles(nombre_archivo):
    f = open(nombre_archivo, encoding='UTF-8')
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    arboleda = [dict(zip(headers, row)) for row in rows]
    return arboleda




os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
altura_jacaranda = [(float(arbol['altura_tot'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
#plt.hist(altura_jacaranda, bins = 30)
altura_jacaranda.sort()
print(altura_jacaranda)


#5.17
medidas_jacaranda = [(float(arbol['altura_tot']), int(arbol['diametro']))
for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(medidas_jacaranda)



def scatter_hd(lista_de_pares):
    lista_de_pares=np.array(lista_de_pares)
    plt.scatter(lista_de_pares[:,0] , lista_de_pares[:,1] ,alpha=0.5, c='RED')
    plt.colorbar(label='Gamma Ray - API')
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()
        
#scatter_hd(medidas_jacaranda)


def medidas_de_especies(especies, arboleda):
    medidas = []
    medidas.append([{e:(float(arbol['altura_tot']), int(arbol['diametro']))}for e in especies for arbol in arboleda if arbol['nombre_com'] == e])
    return medidas

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)
scatter_hd(medidas)
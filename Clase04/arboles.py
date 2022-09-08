# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 09:33:24 2022

@author: juani
"""

#%%4.13

import csv 
from pprint import pprint

def leer_parque(nombre_archivo, nombre_parque):
    arboles_parque = []
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)

        for fila in filas:
            record = dict(zip(encabezados, fila))
    
            if record["espacio_ve"] == nombre_parque:
                arboles_parque.append(record)
    return arboles_parque
        

arboles_parque = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'DE LAS VICTORIAS')


#4.14
def especies(lista_arboles):
    especies_arboles = []
    for arbol in lista_arboles:
        especies_arboles.append(arbol['nombre_com'])
    especies_arboles = set(especies_arboles)
    return especies_arboles

especies(arboles_parque)

#4.15
from collections import Counter
arboles_generalpaz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
arboles_losandes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
arboles_centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

def contar_ejemplares(lista_arboles):
    total_arboles=[]
    for arbol in lista_arboles:
        nombre_arbol = arbol['nombre_com']
        total_arboles.append(nombre_arbol)
    lista_arb = Counter(total_arboles)
    print('las cinco especies mas frecuentes son',lista_arb.most_common(5))
    
# contar_ejemplares(arboles_generalpaz)
# contar_ejemplares(arboles_centenario)
# contar_ejemplares(arboles_losandes)
#4.16
def maximo(lista):
    maximo=max(lista, key=(float))
    return maximo

def mean(lista):
    lista=list(map(int, lista))
    return sum(lista)/len(lista)

arboles_generalpaz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
def obtener_alturas(lista_arboles, especie):
    altura_especie=[]
    prom=0.0
    for arbol in lista_arboles:
       if(arbol['nombre_com']==especie):
           altura_especie.append(arbol['altura_tot'])

    maxx = maximo(altura_especie)
    prom=mean(altura_especie)
    print(maxx,prom)
    
    
obtener_alturas(arboles_generalpaz, 'Jacarandá')
obtener_alturas(arboles_centenario, 'Jacarandá')
obtener_alturas(arboles_losandes, 'Jacarandá')
#4.17
def obtener_inclinacion(lista_arboles, especie):
    inclinacion_especie=[]
    for arbol in lista_arboles:
       if(arbol['nombre_com']==especie):
           inclinacion_especie.append(arbol['inclinacio'])
    print('las inclinaciones',inclinacion_especie)
obtener_inclinacion(arboles_generalpaz, 'Jacarandá')
#4.18
#4.19

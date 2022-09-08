# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 07:42:05 2022

@author: juani
"""
import csv 

def leer_arboles(nombre_archivo):
    f = open(nombre_archivo, encoding='UTF-8')
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    arboleda = [dict(zip(headers, row)) for row in rows]
    return arboleda

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
#5.16
H=[float(arbol['altura_tot']) for arbol in arboleda]

altura_jacaranda = [float(arbol['altura_tot'])
    for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print('Altura Jacarandá:', altura_jacaranda)
#5.17
medidas_jacaranda = [(float(arbol['altura_tot']), int(arbol['diametro']))
for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(medidas_jacaranda)
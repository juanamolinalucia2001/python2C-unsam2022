# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 07:24:34 2022

@author: juani
"""
#nombre ARCHIVO  busqueda_en_listas.py

# Búsqueda de máximo y mínimo
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e>m:
            m=e
    return m

print(maximo([1,2,-7,2,3,4]))
print(maximo([1,2,3,4]))
print(maximo([-5,-4]))

def minimo(lista):
    m = 0 
    for e in lista: 
        if e<m:
            m = e
    return m

print(minimo([1,2,-7,2,3,4]))
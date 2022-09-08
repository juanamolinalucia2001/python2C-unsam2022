# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 07:41:28 2022

@author: juani
"""

#5.4
def invertir_lista(lista):
    invertida = []
    largo=len(lista)
    for e in lista: # Recorro la lista
        largo-=1
        invertida.append(lista[largo])  #agrego el elemento e al principio de la lista invertida
    return invertida


print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))

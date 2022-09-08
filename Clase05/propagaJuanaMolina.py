# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 07:41:47 2022

@author: juani
"""

def propagar(lista):
    i=1
    while i < len(lista)-1:
        if lista[i]==1 and lista[i+1]==0:
            lista[i+1]=1
    
        if lista[i]==1 and lista[i-1]==0:
            lista[i-1] = 1
            i= i-2
        i= i+1
    return(lista)

print(propagar([ 0, 0, 0, 1, 1, 0]))
print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
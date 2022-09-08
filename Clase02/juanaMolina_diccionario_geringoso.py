# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 17:05:29 2022

@author: juani
"""

def traducir(palabra):
    cadena = ""
    for c in palabra:
        if c in "aeiou":
            cadena = cadena + c + "p"+ c
        else:
            cadena = cadena + c
    return cadena

def agregar_diccionario(lista):
    diccionario = {}
    for l in lista:
       diccionario[l]=traducir(l)
    print(diccionario)
        
lista=['banana', 'manzana', 'mandarina']
agregar_diccionario(lista)
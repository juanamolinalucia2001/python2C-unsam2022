# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 18:38:48 2022

@author: juani
"""

#%%Funciones 2.7 Transformar un script en una función
def buscar_precio(fruta):
        precio=0    
        encontrado=False
        for line in f:
            row = line.split(',')
            if(row[0] == fruta):
                encontrado=True
                precio=row[1]
        return encontrado, precio
              


f = open('Data/precios.csv', 'rt')
headers = next(f).split(',')
fruta=input("ingrese fruta que desea saber el precio:")
encontrado, precio = buscar_precio(fruta)
if(encontrado):
    print('El precio de la fruta es ', precio)
else: 
    print("no esta la fruta")

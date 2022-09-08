# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 20:35:17 2022

@author: juani
"""

import csv

def leer_camion(nombre_archivo1):
    camion=[]
    with open(nombre_archivo1,'rt') as f:
         rows=csv.reader(f)
         headers=next(rows)
         for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    return camion



def leer_precios(nombre_archivo2):
    precios={}
    with open(nombre_archivo2, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = (row[1])
            except IndexError:
                print('Faltan datos en la línea', row,'del archivo')
        return precios
    





def balance(nombre_archivo1, nombre_archivo2):
    camion = leer_camion(nombre_archivo1)
    precios = leer_precios(nombre_archivo2)
    pagado_productor = 0.0
    precio_mercado = 0.0   
    balance=0.0
    for nombre, cajones, precio in camion:
        pagado_productor+= cajones*precio
        precio_mercado += float(precios[nombre])*int(cajones)
        balance = precio_mercado - pagado_productor
    return (balance)

balance('../Data/camion.csv','../Data/precios.csv')
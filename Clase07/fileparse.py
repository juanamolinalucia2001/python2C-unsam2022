# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:04:24 2022

@author: juani
"""

# fileparse.py

import csv

def parse_csv(nombre_archivo, select = None, types=None,has_headers=True):
    
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        #chequeo que tenga encabezado
        if has_headers:
            # Lee los encabezados del archivo
            encabezados = next(filas)
    
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
    
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                 #Parseo    
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
    
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
                
        if not has_headers:
            registros = []
            for fila in filas:
               if not fila:    # Saltear filas vacías
                   continue
               if fila:
                   fila = (fila[0], fila[1])
               if types:
                   fila = (types[0](fila[0]), types[1](fila[1]))
           
               registros.append(fila)
                

    return registros

#camion_fruta_precio = parse_csv('../Data/camion.csv', select=['nombre','precio'])
#camion = parse_csv('../Data/camion.csv', types=[str, int, float])
# precios = parse_csv('../Data/precios.csv', types=[str, float], has_headers=False)
# print(camion_fruta_precio,camion)
# print(precios)

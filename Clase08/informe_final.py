# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 08:41:20 2022

@author: juani
"""

#8.7
import csv

from fileparse import parse_csv

def leer_camion(archivo):
    with open(archivo) as f:
        contenido_camion= parse_csv(f, has_headers=True)
        return contenido_camion


def leer_precios(archivo):
    with open(archivo) as f:
        lista_precios= parse_csv(f, has_headers=False)
    return lista_precios


def imprimir_informe(nombre_archivo1,nombre_archivo2):
    camion = leer_camion(nombre_archivo1)
    precios = leer_precios(nombre_archivo2)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    sep = ('----------')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s}')
    for s in camion:
        lista = ((s['nombre'], s['cajones'], '$' + str(s['precio']), precios[0][1] - s['precio']))
        print('%10s %10d %10s %10.2f' % lista)

        
# def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
#     leer_camion(nombre_archivo_camion)
#     leer_precios(nombre_archivo_precios)
#     imprimir_informe(nombre_archivo_camion, nombre_archivo_precios)

# camion=leer_camion('../Data/camion.csv')

# precio=leer_precios('../Data/precios.csv')
informe=imprimir_informe('../Data/camion.csv','../Data/precios.csv')
# informe_camion('../Data/fecha_camion.csv','../Data/precios.csv')
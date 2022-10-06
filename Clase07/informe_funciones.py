# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:05:15 2022

@author: juani
"""
#%%
#7.8 como importar modulos

# import sys
# import rebotes
# import hipoteca
# import informe_funciones


from fileparse import parse_csv
camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
 #%%
import csv

from fileparse import parse_csv

def leer_camion(archivo):
    contenido_camion = parse_csv(archivo, select=['nombre','cajones','precio'], types=[str, int, float])
    return contenido_camion



def leer_precios(archivo):
    lista_precios = parse_csv(archivo, types=[str, float], has_headers = False)
    return lista_precios

#7.2
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
        
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    leer_camion(nombre_archivo_camion)
    leer_precios(nombre_archivo_precios)
    imprimir_informe(nombre_archivo_camion, nombre_archivo_precios)

imprimir_informe('../Data/camion.csv','../Data/precios.csv')
# informe_camion('../Data/fecha_camion.csv','../Data/precios.csv')
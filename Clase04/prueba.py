# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 17:51:22 2022

@author: juani
"""

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
 headers=('Nombre', 'Cajones', 'Precio', 'Cambio')
 sep = ('----------')
 print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
 print(f'{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s}')
 lista=[]
 for nombre, cajones, precio in camion:
        lista=(nombre,cajones,precio,float(precios[nombre]) - precio )
        print('%10s %10d %10s %10.2f' % lista)

balance('../Data/camion.csv','../Data/precios.csv')
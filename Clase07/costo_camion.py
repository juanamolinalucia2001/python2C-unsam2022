# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:05:25 2022

@author: juani
"""

#import costocamion_juanaMolina

from  informe_funciones import leer_camion

def costo_camion(nombre_archivo):
    camion = leer_camion(nombre_archivo)
    lista=[]
    for fila in camion:
        lista.append((fila['cajones'])*(fila['precio']))
    print(lista)
    print(sum(lista))
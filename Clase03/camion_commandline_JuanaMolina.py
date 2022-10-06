# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 20:35:17 2022

@author: juani
"""

import csv
import sys

def costo_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        total = 0
        try:
            for row in rows:
                total += int(row[1]) * float(row[2])
        except ValueError:
            print(f"En la fila {row} Hubo un error")
            
        return total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

    
costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
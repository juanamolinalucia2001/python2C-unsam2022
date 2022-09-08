# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 09:05:04 2022

@author: juani
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 13:53:45 2022
@author: datascience
"""
#%%4.4
import csv
path="/home/datascience/Descargas/Ejercicios/ejercicios_python/Data/fecha_camion.csv"
def costo_camion(nombre_archivo):
    costo_total=0.0
    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezados = next(filas)
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        print(record)
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
            
    print(costo_total)
    
    
costo_camion('../Data/fecha_camion.csv')
    


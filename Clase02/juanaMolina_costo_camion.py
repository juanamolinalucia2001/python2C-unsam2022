# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:25:42 2022

@author: juani
"""
import csv
f = open('Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
suma=0
for row in rows:
   suma=suma+(float(row[1])*float(row[2]))
print('Costo total',suma)
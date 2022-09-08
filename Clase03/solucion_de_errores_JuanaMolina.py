# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:40:44 2022

@author: juani
"""

#%%3.5
#linea 13 tranformo la exprecion a minusculas en caso de no hacerlo la A mayuscula no esta contemplada
#linea 21 cambio return false por i+=1  por si la primera palabra no es 'a' no seguia iterando y devolvia false
#linea 22 return false identado a la altura del while 
def tiene_a(expresion):
    expresion = expresion.lower()
    print(expresion)
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            i += 1
    return False
    
print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
#%%3.6
#32,35y 36 y agregar ":" en el if faltaba un = si hay uno solo seria de asignacion con == es de comparacion
#39  cambiar el return Falso por False

def tiene_a(expresion):
    expresion = expresion.lower()
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%3.7
def tiene_uno(expresion):
    #paso expresion a str para reconocer los valores de ambos tipos
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))
#%%3.8
def suma(a,b):
   # c = a + b /retornar suma y borrar asignacion de c ya que se hace mas abajo
   return a+b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
#%%3.9
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    #registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
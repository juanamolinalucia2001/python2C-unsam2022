# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:18:35 2022

@author: juani
"""
import random

#6.5
# Escribí un programa estimar_pi.py que genere cien mil puntos aleatorios con la función generar_punto(), calcule la proporción
#  de estos puntos que caen en el círculo unitario (usando ¿x^2 + y^2 < 1?) y use este resultado para dar una aproximación de pi.
def generar_punto():
    x = random.random()
    y = random.random()
    return x,y
#%%6.6
# Hagamos algún ejercicio sencillo antes de terminar. Supongamos que una persona se compra un termómetro que mide la temperatura con un error aleatorio 
#de distribución normal con media 0 y desvío estándar de 0.2 grados (error gaussiano). Si la temperatura real de la persona es de 37.5 grados, simulá
# usando normalvariate() (con mu y sigma adecuados) n valores medidos por el termómetro. Escribí una función llamada medir_temp(n) que simule n mediciones y las devuelva en una lista.

# Escribí una función llamada resumen_temp(n) que realice una simulación de n temperaturas (usando la función medir_temp(n)) y devuelva una tupla con el valor máximo, el mínimo, el promedio y la mediana (en ese orden) de estas n mediciones. Guardá tu script en el archivo termometro.py.
import random
import statistics
import numpy as np

def medir_temp(n):
    mediciones=[]
    for i in range(n):
        mediciones.append(round(random.normalvariate(37.5, 0.2), 2))
    return mediciones

def resumen_temp(lista):
    lista.sort()
    print(lista)
    maximo=max(lista)
    minimo=min(lista)
    promedio=sum(lista)/len(lista)
    print('Valor máximo:', maximo)
    print('Valor mìnimo:', minimo)
    print('Valor promedio:', promedio)
    print('Mediana mediciones:', statistics.median(lista))
    

dataMediciones=np.array(medir_temp(999))
np.save('../Data/temperaturas.npy', dataMediciones)

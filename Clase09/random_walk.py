# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:33:50 2022

@author: juani
"""

#%%9.2
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)
    return pasos.cumsum()
lista=[]
N = 100000

for i in range(12):
   n =randomwalk(N) 
   lista.append(n)
   plt.plot(n)
   plt.ylabel('tiempo')
   plt.xlabel('distancia al origen')

plt.show()
print(lista)
listaAbsMax=[]
listaAbsMin=[]

for a in lista:
    listaAbsMax.append(max(abs(a)))
print(listaAbsMax)
rey_max=np.argmax(listaAbsMax)

plt.subplot(1,2,1)
plt.plot(lista[rey_max],color="violet")


for b in lista:
    listaAbsMin.append(min(abs(b)))
print(listaAbsMin)
rey_min=np.argmin(listaAbsMin)
plt.subplot(1,2,2)
plt.plot(lista[rey_min],color="red")
plt.show()
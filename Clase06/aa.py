# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 08:42:53 2022

@author: juani
"""

# r=[x*y for x in range(-10,10) if x > 0 and x%2==1 for y in [1,0,-1] if y!=0]

# for x in range(-10,10):
#     if x > 0 and x%2==1:
#         for y in [1,0,-1]:
#             if y!=0:
#                 print(x*y)
                
# #%%
# a=['n','e','p']
# b=['R',43,78]
# d=dict(zip(a,b))


# #%%
# # for i , c in enumerate('pavada'):
# #     if i!=(i//2)*2:
# #         print(c, end='')
        
# #%%
# i=0
# suma=0
# while i<=10:
#     suma+=0

# print(suma)
# #%%
# d={}
# dias=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
# dias_abreviados=['lu','ma','mi','ju','vi','sa','do']
# while len(d) < 6:
#     dia=dias[len(d)]
#     abr=dias_abreviados[len(d)]
#     d[dia]=abr

# print(d['sabado'])

# #%%
# import numpy as np
# a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# b=a[1:3]
#%%

# def func(a):
#     a+=1
    
# a=1
# a=func(a)
# a=a+1
# #%%
# lista=[2,4,6,8,10]
# {x:x**2 for x in range(10) if x in lista}
#%%
def func(a,b):
    c=a+b
    return c
print   (func(2,3))


# c=3
# c=func(2, 3)

# n=5
# lista=[1]*n
# for i in range(1,n):
#     lista[i]= lista[i-1]+ lista[i]+ lista[i+1]
#     print(lista)
    
#%% jajaja
lista=[1,2,3]
n=2
try:
   for k in range(10): 
    if  lista[k]==3 and k<n:
        print('caso1')
except Exception:
    print('caso2')
    
#%%
import random
random.random()
#%%
tupla=(1,3,4,5,7)

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:11:19 2022

@author: juani
"""

#8.8
def valor_absoluto(n):
    if n >= 0:
        return n
    else:
        return -n
    
'''Cálculo del valor absoluto

    Pre: Recibe un número real.
    Pos: Devuelve un número nat , que es el valor absoluto .
   
    '''
#%%
def suma_pares(l):
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

'''Cálculo la suma de los valores pares de la lista

    Pre: Recibe una lista con numeros reales.
    Pos: Devuelve un número real , que es la suma de todos los num pares de la lista.
    
    invariante: e debe estar en la lista, si la lista es vacia no itera nunca
    '''

#%%
def veces(a, b):
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

a=veces(1, 10)
'''
    Pre: Recibe dos nùmeros a real b nat .
    Pos: Devuelve un número real , que es la suma a las b veces osea a=1 b=10 retorna 10.
    
    invariante: nb distinto del cero b numero nat por que sino itera inf veces.
    '''
#%%
def collatz(n):
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

'''
    Pre: Recibe un numero .
    Pos: Devuelve un número real , que es la suma a las b veces osea a=1 b=10 retorna 10.
    
    invariante: n distinto de 1.
    '''
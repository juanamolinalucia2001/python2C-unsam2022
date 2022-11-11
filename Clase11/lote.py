# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:45:53 2022

@author: juani
"""

class Lote:
    def __init__(self,nombre,cajones,precio):
        self.nombre=nombre
        self.cajones=cajones
        self.precio=precio
        
    def costo(self):
        return self.cajones * self.precio
     
    def vender(self,cantidad):
        self.cajones-=cantidad
        
    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'
        
a = Lote('pera', 5, 5)

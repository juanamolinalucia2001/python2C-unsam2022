# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:25:59 2022

@author: juani
"""
import os

def archivos_png(directorio):
    for root, dirs, files in os.walk(directorio):
       for name in files:
         if name.endswith('.png'):
          return name
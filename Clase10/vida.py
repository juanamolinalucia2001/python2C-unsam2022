# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:13:48 2022

@author: juani
"""
from datetime import datetime

# en formato mm/dd/YY 
def vida_en_segundos(fecha_nac):
    fecha_nac = datetime.strptime(fecha_nac, '%d/%m/%Y')    
    fecha_nacimiento = fecha_nac
    fecha_actual= datetime.today()
    segundos_vividos = fecha_nacimiento - fecha_actual
    return segundos_vividos.total_seconds()
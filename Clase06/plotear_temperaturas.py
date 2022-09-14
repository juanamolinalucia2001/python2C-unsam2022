# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:11:50 2022

@author: juani
"""
import numpy as np

def plotear_temperaturas(temperaturas):
    import matplotlib.pyplot as plt
    plt.hist(temperaturas,bins=50)
    plt.show()
    
temperaturas = np.load('../Data/temperaturas.npy')
plotear_temperaturas(temperaturas)
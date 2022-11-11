# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:46:20 2022

@author: juani
"""

#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Thu Nov  3 13:36:03 2022

@author: datascience
"""

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def init(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


class TorreDeControl(Cola):

    def init(self):
        self.vuelos_des=Cola()
        self.vuelos_arr=Cola()

    def nuevo_arribo(self,nombre):
        self.vuelos_arr.encolar(nombre)

    def nueva_partida(self,nombre):
        self.vuelos_des.encolar(nombre)

    def ver_estado(self):
        print (f'({self.vuelos_des.items},{self.vuelos_arr.items})' )



    def asignar_pista(self):

        if not self.vuelos_arr.esta_vacia():
            self.vuelos_arr.desencolar()
            print (f'({self.vuelos_des.items},{self.vuelos_arr.items})' )

        elif not self.vuelos_des.esta_vacia():
            self.vuelos_des.desencolar()
            print (f'({self.vuelos_des.items},{self.vuelos_arr.items})' )

        else:
            print('no hay vuelos en espera')


torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
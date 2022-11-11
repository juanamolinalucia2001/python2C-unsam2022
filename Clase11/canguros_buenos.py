# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:46:07 2022

@author: juani
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:31:49 2022

@author: datascience
"""

"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        #Aca estaba el problema .En la lista contenido se estaba referenciando
        # a la lista del objeto anterior en este caso mamaCanguro,por lo tanto en cangurito se repetian los valores,
        #usando un copy hacemos referencia a la lista vacia y solucionamos el error 
        self.contenido_marsupio = contenido.copy()

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito.nombre)

print(madre_canguro)
print(cangurito)
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:35:55 2022

@author: juani
"""

#9.8
import pandas as pd
import os

#leo datos de parque
directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df_parques = pd.read_csv(fname)

#leo datos de veredas
dire = '../Data'
arch = 'arbolado-publico-lineal-2017-2018.csv'
fname1 = os.path.join(dire,arch)
veredas = pd.read_csv(fname1)

#renombro las variables del datset veredas para que coincida con el de parques
df_veredas=veredas.rename(columns={"diametro_altura_pecho": "diametro", "nombre_cientifico": "nombre_cie","altura_arbol":"altura_tot"})

#eligo las columnas 
cols_parques = ['altura_tot', 'diametro' ,'nombre_cie']
cols_veredas=['altura_tot', 'diametro' , 'nombre_cie' ]
        
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_parques].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cie'] == 'Tipuana tipu'][cols_veredas].copy()


new_df_tipas_parques=df_tipas_parques.assign(ambiente='parque')
new_df_tipas_veredas=df_tipas_veredas.assign(ambiente='vereda')


df_tipas = pd.concat([new_df_tipas_parques, new_df_tipas_veredas])
df_tipas.boxplot('diametro',by = 'ambiente')
df_tipas.boxplot('altura_tot',by = 'ambiente')

#¿Qué tendrías que cambiar para repetir el análisis para otras especies? ¿Convendría definir una función?
#cambiar en la linea 31 y 32 la especie que se desea analizar
#si convendria una funcion porq sino estariamos repitiendo mucho codigo para volver analizar otra especie en cambio si tenemos una función
#df_arbolQuebusco=def plotearEspecie(le paso el arbol que quiero ) y listo 
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 23:43:57 2019

@author: Cristian
"""

from ..database.HyberGrings import HyberGrings

#%%

class ModeloVeiculo(HyberGrings):
    
    def __init__(self,dados=None):
        self.__id_modelo_Veiculo = None
        self.__modelo   = None
        self.__marca    = None
        self.__ano       = None
        super(ModeloVeiculo, self).__init__(self.__class__.__name__, self.__dict__)

        if dados:
            self.fromTuple(dados)

    
    @property
    def id_modelo_Veiculo(self):
        return self.__id_modelo_Veiculo
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo
        self.update()

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,marca):
        self.__marca = marca
        self.update()
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self,ano):
        self.__ano = ano
        self.update()
    
    def __str__(self):
        return "{"f""" ---------------ModeloVeiculo---------------
        'id_modelo_Veiculo':\t'{self.__id_modelo_Veiculo}'
        'modelo':\t'{self.__modelo}'
        'marca':\t'{self.__marca}'
        'ano':\t'{self.__ano}'""""}"
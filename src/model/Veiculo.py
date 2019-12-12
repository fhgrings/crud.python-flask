# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:35:54 2019

@author: Cristian
"""

from ..database.HyberGrings import HyberGrings

#%%

class Veiculo(HyberGrings):

    def __init__(self,dados=None):
        self.__renavan              = None
        self.__placa                = None
        self.__id_modelo_veiculo    = None
        super(Veiculo, self).__init__(self.__class__.__name__, self.__dict__)
        if dados:
            self.fromTuple(dados)

    
    @property
    def renavan(self):
        return self.__renavan
    
    @property
    def placa(self):
        return self.__placa
    
    @placa.setter
    def placa(self,placa):
        self.__placa = placa
        self.update()

    @property
    def id_modelo_veiculo(self):
        return self.__id_modelo_veiculo
    
    @id_modelo_veiculo.setter
    def id_modelo_veiculo(self,id_modelo_veiculo):
        self.__id_modelo_veiculo = id_modelo_veiculo
        self.update()
    
    def __str__(self):
        return "{"f"""
        "renavan":\t"{self.__renavan}",
        "placa":\t"{self.__placa}",
        "id_modelo_veiculo":\t"{self.__id_modelo_veiculo}" """"}"
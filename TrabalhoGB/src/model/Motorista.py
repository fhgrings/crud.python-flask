# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:26:12 2019

@author: Cristian
"""

from ..database.HyberGrings import HyberGrings

#%%

class Motorista(HyberGrings):
    
    def __init__(self,dados=None):
        self.__id_motorista = None
        self.__CPF_condutor   = None
        self.__renavan    = None
        self.__data_inicio       = None
        self.__data_fim       = None
        super(Motorista, self).__init__(self.__class__.__name__, self.__dict__)

        if dados:
            self.fromTuple(dados)

    
    @property
    def id_motorista(self):
        return self.__id_motorista
    
    @property
    def CPF_condutor(self):
        return self.__CPF_condutor
    
    @CPF_condutor.setter
    def CPF_condutor(self,CPF_condutor):
        self.__CPF_condutor = CPF_condutor
        self.update()

    @property
    def renavan(self):
        return self.__renavan
    
    @renavan.setter
    def renavan(self,renavan):
        self.__renavan = renavan
        self.update()
        
    @property
    def data_inicio(self):
        return self.__data_inicio
    
    @data_inicio.setter
    def data_inicio(self,data_inicio):
        self.__data_inicio = data_inicio
        self.update()
        
    @property
    def data_fim(self):
        return self.__data_fim
    
    @data_fim.setter
    def data_fim(self,data_fim):
        self.__data_fim = data_fim
        self.update()
    
    def __str__(self):
        return "{"f"""
        "id_motorista":\t"{self.__id_motorista}",
        "CPF_condutor":\t"{self.__CPF_condutor}",
        "renavan":\t"{self.__renavan}",
        "data_inicio":\t"{self.__data_inicio}",
        "data_fim":\t"{self.__data_fim}" """"}"
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:06:45 2019

@author: Cristian
"""

from ..database.HyberGrings import HyberGrings
#%%

class InformacoesCorrida(HyberGrings):
    
    def __init__(self,dados=None):
        self.__CPF_condutor          = None
        self.__Nome                  = None
        self.__CPF_passageiro        = None
        self.__nome                  = None
        self.__origem                = None
        self.__destino               = None
        self.__distancia             = None
        self.__Valor                 = None
        self.__Duracao               = None
        self.__renavan               = None
        self.__placa                 = None
        self.__marca                 = None
        self.__ano                   = None
        super(InformacoesCorrida, self).__init__(self.__class__.__name__, self.__dict__)

        if dados:   
            self.fromTuple(dados)     
            
    
    def __str__(self):
        return f""" ---------------Corrida---------------
        CPF_condutor:\t{self.__CPF_condutor}
        Nome:\t{self.__Nome}
        CPF_passageiro:\t{self.__CPF_passageiro}
        nome:\t{self.__nome}
        origem:\t{self.__origem}
        destino:\t{self.__destino}
        distancia:\t{self.__distancia}
        Valor:\t{self.__Valor}
        Duracao:\t{self.__Duracao}
        renavan:\t{self.__renavan}
        placa:\t{self.__placa}
        marca:\t{self.__marca}
        ano:\t{self.__ano}"""
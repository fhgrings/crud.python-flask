# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:55:41 2019

@author: Cristian
"""
    
from ..database.HyberGrings import HyberGrings

#%%

class InformacoesVeiculo(HyberGrings):
    def __init__(self,dados=None):
        self.__placa                  = None
        self.__renavan                = None
        self.__modelo                 = None
        self.__marca                  = None
        self.__ano                    = None
        self.__QuantidadeCorridas     = None
        self.__QuantidadeAvalicoes    = None
        self.__Med_Avaliacao_Veiculo  = None
        super(InformacoesVeiculo, self).__init__(self.__class__.__name__, self.__dict__)

        if dados:
            self.fromTuple(dados)     
            

    def __str__(self):
        return f""" ---------------InformacoesVeiculo---------------
        Placa:\t{self.__placa}
        Renavan:\t{self.__renavan}
        Modelo:\t{self.__modelo}
        Marca:\t{self.__marca}
        Ano:\t{self.__ano}
        Quantidade Corridas:\t{self.__QuantidadeCorridas}
        Quantidade Avalicoes:\t{self.__QuantidadeAvalicoes}
        Med_Avaliacao_Veiculo:\t{self.__Med_Avaliacao_Veiculo}"""
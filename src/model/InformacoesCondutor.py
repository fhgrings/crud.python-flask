# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:47:05 2019

@author: Cristian
"""

from ..database.HyberGrings import HyberGrings

#%%

class InformacoesCondutor(HyberGrings):
    def __init__(self,dados=None):
        self.__CPF_condutor          = None
        self.__Nome                  = None
        self.__QuantidadeAvalicoes   = None
        self.__Media_avaliacoes      = None
        self.__Quantidade_Corridas   = None
        self.__Pagamento             = None
        super(InformacoesCondutor, self).__init__(self.__class__.__name__, self.__dict__)
        if dados:
            self.fromTuple(dados)     
            
    def __str__(self):
        return "{ " f"""
        "CPF condutor":\t"{self.__CPF_condutor}",
        "Nome condutor":\t"{self.__Nome}",
        "Quantidade Avalicoes":\t"{self.__QuantidadeAvalicoes}",
        "Media Avaliacoes":\t"{self.__Media_avaliacoes}",
        "Quantidade Corridas":\t"{self.__Quantidade_Corridas}",
        "Pagamento":\t"{self.__Pagamento}" """ "}"
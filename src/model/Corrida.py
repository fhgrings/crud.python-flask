# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:03:23 2019

@author: Cristian
"""
    
from ..database.HyberGrings import HyberGrings

#%%

class Corrida(HyberGrings):
    
    def __init__(self,dados=None):
        self.__id_corrida            = None
        self.__id_motorista          = None
        self.__CPF_passageiro        = None
        self.__avaliacao_condutor    = None
        self.__avaliacao_veiculo     = None
        self.__data_inicio           = None
        self.__data_fim              = None
        self.__origem                = None
        self.__destino               = None
        self.__tarifa                = None
        self.__distancia             = None
        super(Corrida, self).__init__(self.__class__.__name__, self.__dict__, primaryKeys = 3)
        if dados:
            self.fromTuple(dados)

    
    @property
    def id_corrida(self):
        return self.__id_corrida
    
    @id_corrida.setter
    def id_corrida(self,id_corrida):
        self.__id_corrida = id_corrida
        self.update()

    @property
    def id_motorista(self):
        return self.__id_motorista
    
    @property
    def CPF_passageiro(self):
        return self.__CPF_passageiro
    
    @CPF_passageiro.setter
    def CPF_passageiro(self,CPF_passageiro):
        self.__CPF_passageiro = CPF_passageiro
        self.update()
        
    @property
    def avaliacao_condutor(self):
        return self.__avaliacao_condutor
    
    @avaliacao_condutor.setter
    def avaliacao_condutor(self,avaliacao_condutor):
        self.__avaliacao_condutor = avaliacao_condutor
        self.update()
    
    @property
    def avaliacao_veiculo(self):
        return self.__avaliacao_veiculo
    
    @avaliacao_veiculo.setter
    def avaliacao_veiculo(self,avaliacao_veiculo):
        self.__avaliacao_veiculo = avaliacao_veiculo
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
  
    @property
    def origem(self):
        return self.__origem
    
    @origem.setter
    def origem(self,origem):
        self.__origem = origem
        self.update()
    
    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self,destino):
        self.__destino = destino
        self.update()

    @property
    def tarifa(self):
        return self.__tarifa
    
    @tarifa.setter
    def tarifa(self,tarifa):
        self.__tarifa = tarifa
        self.update()
        
    @property
    def distancia(self):
        return self.__distancia
    
    @distancia.setter
    def distancia(self,distancia):
        self.__distancia = distancia
        self.update()        
         
    def __str__(self):
        return "{"f"""
        "id_motorista":\t"{self.__id_motorista}",
        "CPF_passageiro":\t"{self.__CPF_passageiro}",
        "id_corrida":\t"{self.__id_corrida}",
        "avaliacao_condutor":\t"{self.__avaliacao_condutor}",
        "avaliacao_veiculo":\t"{self.__avaliacao_veiculo}",
        "data_inicio":\t"{self.__data_inicio}",
        "data_fim":\t"{self.__data_fim}",
        "origem":\t"{self.__origem}",
        "destino":\t"{self.__destino}",
        "tarifa":\t"{self.__tarifa}",
        "distancia":\t"{self.__distancia}" """"}"
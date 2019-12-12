from ..database.HyberGrings import HyberGrings

class Passageiro(HyberGrings):
    

    def __init__(self,dados=None):
        self.__cpf_passageiro = None
        self.__nome   = None
        self.__telefone    = None
        self.__data_cadastro       = None
        super(Passageiro, self).__init__(self.__class__.__name__, self.__dict__)

        if dados:
            self.fromTuple(dados)


    
    @property
    def cpf_passageiro(self):
        return self.__cpf_passageiro
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
        self.update()

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self,telefone_passageiro):
        self.__telefone= telefone_passageiro
        self.update()
    
    @property
    def data_cadastro(self):
        return self.__data_cadastro
    
    @data_cadastro.setter
    def data_cadastro(self,data_cadastro_passageiro):
        self.__data_cadastro = data_cadastro_passageiro
        self.update()

    def __str__(self):
        return "{"f"""
        "cpf_passageiro":\t"{self.__cpf_passageiro}",
        "nome":\t"{self.__nome}",
        "telefone":\t"{self.__telefone}",
        "data_cadastro":\t"{self.__data_cadastro}" """"}"
from ..model.InformacoesVeiculo import InformacoesVeiculo

class InformacoesVeiculoService():
    def getAll(self, request):
        informacoesVeiculo = InformacoesVeiculo()
        try:
            return informacoesVeiculo.findAll()
        except Exception as e:
            return e
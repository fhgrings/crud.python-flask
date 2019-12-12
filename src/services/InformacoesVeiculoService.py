from ..model.InformacoesVeiculo import InformacoesVeiculo

class InformacoesVeiculoService():
    def getAll(self, request):
        informacoesVeiculo = InformacoesVeiculo()
        try:
            return informacoesVeiculo.findAll()
        except Exception as e:
            return e


    def getOne(self, request):
        informacoesVeiculo = InformacoesVeiculo()
        try:
            informacoesVeiculo.findById(request.args.get('idVeiculo'))
            return informacoesVeiculo.__str__()
        except Exception as e:
            return str(e)
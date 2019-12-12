from ..model.InformacoesCorrida import InformacoesCorrida

class InformacoesCorridaService():
    def getAll(self, request):
        informacoesCorrida = InformacoesCorrida()
        try:
            return str(informacoesCorrida.findAll())
        except Exception as e:
            return str(e)

    def getOne(self, request):
        informacoesCorrida = InformacoesCorrida()
        try:
            informacoesCorrida.findById(request.args.get('idCorrida'))
            return informacoesCorrida.__str__()
        except Exception as e:
            return str(e)
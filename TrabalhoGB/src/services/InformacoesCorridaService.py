from ..model.InformacoesCorrida import InformacoesCorrida

class InformacoesCorridaService():
    def getAll(self, request):
        informacoesCorrida = InformacoesCorrida()
        try:
            return str(informacoesCorrida.findAll())
        except Exception as e:
            return str(e)
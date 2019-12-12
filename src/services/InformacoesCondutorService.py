from ..model.InformacoesCondutor import InformacoesCondutor

class InformacoesCondutorService():
    def getAll(self, request):
        informacoesCondutor = InformacoesCondutor()
        try:
            return informacoesCondutor.findAll().__str__()
        except Exception as e:
            return str(e)

    def getOne(self, request):
        informacoesCondutor = InformacoesCondutor()
        try:
            informacoesCondutor.findById(request.args.get('idCondutor'))
            return informacoesCondutor.__str__()
        except Exception as e:
            return str(e)
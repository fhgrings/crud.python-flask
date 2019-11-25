from ..model.InformacoesCondutor import InformacoesCondutor

class InformacoesCondutorService():
    def getAll(self, request):
        informacoesCondutor = InformacoesCondutor()
        try:
            return informacoesCondutor.findAll()
        except Exception as e:
            return e
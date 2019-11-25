from ..model.Condutor import Condutor
from ..database.Database import Database

class CondutorService():

    def getCondutor(self, request):
        try:
            condutor = Condutor()
            condutor.findById(request.args.get('idCondutor'))
            return condutor.__str__()
        except Exception:
            return "Id não encontrado"

    def createCondutor(self, request):
        condutor = Condutor()
        params = []
        params.append(request.json['CPF_condutor'])
        params.append(request.json['nome'])
        params.append(request.json['telefone'])
        params.append(request.json['data_cadastro'])
        try:
            condutor.create(params)
        except Exception:
            return "Erro ao criar tupla"
        return 'OK'

    def updateCondutor(self, request):
        params = []
        params.append(request.json['CPF_condutor'])
        params.append(request.json['nome'])
        params.append(request.json['telefone'])
        params.append(request.json['data_cadastro'])
        condutor = Condutor(params)
        print(condutor)
        condutor.update()
        return 'OK'
    
    def deleteCondutor(self, request):
        condutor = Condutor()
        condutor.findById(request.args.get('idCondutor'))
        condutor.delete()
        return 'OK'

    def getInformacoesCondutor(self):
        database = Database()
        self.banco, self.cursor = database.connectionFactory()

        self.query = "SELECT * FROM InformacoesCondutor"
        self.cursor.execute(self.query)
        return self.cursor.fetchone()
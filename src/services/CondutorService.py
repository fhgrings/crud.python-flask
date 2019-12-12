from ..model.Condutor import Condutor
from ..database.Database import Database
import datetime
import json

class CondutorService():

    def getAll(self, request):
        try:
            condutor = Condutor()
            condutores = [Condutor(dados=item).__str__() for item in condutor.findAll()]
            return condutores.__str__()

        except Exception as e:
            return str(e)


    def getCondutor(self, request):
        try:
            condutor = Condutor()
            condutor.findById(request.args.get('idCondutor'))
            return condutor.__str__()
        except Exception:
            return "Id não encontrado", 400

    def createCondutor(self, request):
        condutor = Condutor()
        params = []
        try:
            params.append(request.json['CPF_condutor'])
            params.append(request.json['nome'])
            params.append(request.json['telefone'])
            params.append(request.json['data_cadastro'])
            condutor.create(params)
        except Exception as e:
            return str(e), 400
        return 'OK'

    def updateCondutor(self, request):
        params = []
        try:
            params.append(request.json['CPF_condutor'])
            params.append(request.json['nome'])
            params.append(request.json['telefone'])
            params.append(request.json['data_cadastro'])
            condutor = Condutor(params)
            print(condutor)
            condutor.update()
        except Exception as e:
            return str(e), 400
        return 'OK'
    
    def deleteCondutor(self, request):
        condutor = Condutor()
        try:
            condutor.findById(request.args.get('idCondutor'))
            print(condutor)
            condutor.delete()
            return 'OK'
        except Exception as e:
            return str(e), 400

    def getInformacoesCondutor(self):
        database = Database()
        self.banco, self.cursor = database.connectionFactory()

        self.query = "SELECT * FROM InformacoesCondutor"
        self.cursor.execute(self.query)
        return self.cursor.fetchone()
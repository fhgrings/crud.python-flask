from ..model.Passageiro import Passageiro

class PassageiroService():
    def getPassageiro(self, request):
        passageiro = Passageiro()
        try:
            passageiro.findById(request.args.get('idPassageiro'))
        except Exception as e:
            return str(e), 400
        return passageiro.__str__()

    def createPassageiro(self, request):
        passageiro = Passageiro()
        params = []
        params.append(request.json['cpf_passageiro'])
        params.append(request.json['nome'])
        params.append(request.json['telefone'])
        params.append(request.json['data_cadastro'])

        try:
            passageiro.create(params)
        except Exception as e:
            return str(e), 400
        return 'OK'

    def updatePassageiro(self, request):
        params = []
        params.append(request.json['cpf_passageiro'])
        params.append(request.json['nome'])
        params.append(request.json['telefone'])
        params.append(request.json['data_cadastro'])

        try:
            passageiro = Passageiro(params)
            passageiro.update()
        except Exception as e:
            return str(e), 400
        return 'OK'
    
    def deletePassageiro(self, request):
        passageiro = Passageiro()

        try:
            passageiro.findById(request.args.get('idPassageiro'))
            print(passageiro)
            passageiro.delete()
        except Exception as e:
            return str(e), 400
        return 'OK'


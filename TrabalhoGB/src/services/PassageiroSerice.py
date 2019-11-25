from ..model.Passageiro import Passageiro

class PassageiroService():
    def getPassageiro(self, request):
        passageiro = Passageiro()
        passageiro.findById(request.args.get('idPassageiro'))
        return passageiro.__str__()

    def createPassageiro(self, request):
        passageiro = Passageiro()
        params = []
        params.append(request.json['cpf_passageiro'])
        params.append(request.json['nome'])
        params.append(request.json['telefone'])
        params.append(request.json['data_cadastro'])
        passageiro.create(params)
        return 'OK'

    def updatePassageiro(self, request):
        params = []
        params.append(request.json['cpf_passageiro'])
        params.append(request.json['nome'])
        params.append(request.json['telefone'])
        params.append(request.json['data_cadastro'])
        passageiro = Passageiro(params)
        passageiro.update()
        return 'OK'
    
    def deletePassageiro(self, request):
        passageiro = Passageiro()
        passageiro.findById(request.args.get('idPassageiro'))
        passageiro.delete()
        return 'OK'


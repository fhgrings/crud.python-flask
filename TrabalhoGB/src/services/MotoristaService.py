from ..model.Motorista import Motorista

class MotoristaService():
    def getMotorista(self, request):
        motorista = Motorista()
        motorista.findById(request.args.get('idMotorista'))
        return motorista.__str__()

    def createMotorista(self, request):
        motorista = Motorista()
        params = []
        params.append(request.json['id_motorista'])
        params.append(request.json['CPF_condutor'])
        params.append(request.json['renavan'])
        params.append(request.json['data_inicio'])
        params.append(request.json['data_fim'])
        motorista.create(params)
        return 'OK'

    def updateMotorista(self, request):
        params = []
        params.append(request.json['id_motorista'])
        params.append(request.json['CPF_condutor'])
        params.append(request.json['renavan'])
        params.append(request.json['data_inicio'])
        params.append(request.json['data_fim'])
        motorista = Motorista(params)
        motorista.update()
        return 'OK'
    
    def deleteMotorista(self, request):
        motorista = Motorista()
        motorista.findById(request.args.get('idMotorista'))
        motorista.delete()
        return 'OK'

from ..model.Motorista import Motorista

class MotoristaService():
    def getMotorista(self, request):
        motorista = Motorista()
        try:
            motorista.findById(request.args.get('idMotorista'))
        except Exception as e:
            return str(e), 400
        return motorista.__str__()

    def createMotorista(self, request):
        motorista = Motorista()
        params = []
        params.append(request.json['id_motorista'])
        params.append(request.json['CPF_condutor'])
        params.append(request.json['renavan'])
        params.append(request.json['data_inicio'])
        params.append(request.json['data_fim'])
        try:
            motorista.create(params)
        except Exception as e:
            return str(e), 400
        return 'OK'

    def updateMotorista(self, request):
        params = []
        params.append(request.json['id_motorista'])
        params.append(request.json['CPF_condutor'])
        params.append(request.json['renavan'])
        params.append(request.json['data_inicio'])
        params.append(request.json['data_fim'])

        try:
            motorista = Motorista(params)
            motorista.update()
        except Exception as e:
            return str(e), 400
        return 'OK'

    
    def deleteMotorista(self, request):
        motorista = Motorista()
        try:
            motorista.findById(request.args.get('idMotorista'))
            motorista.delete()
        except Exception as e:
            return str(e), 400
        return 'OK'

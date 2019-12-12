from ..model.Corrida import Corrida

class CorridaService():

    def getCorrida(self, request):
        corrida = Corrida()
        try:
            corrida.findById(request.args.get('idCorrida'))
        except Exception as e:
            return str(e), 400
        return corrida.__str__()

    def getAll(self,request):
        corrida = Corrida()
        corridas = [Corrida(dados=item).__str__() for item in corrida.getAll()]
        return corridas.__str__()

    def createCorrida(self, request):
        corrida = Corrida()
        params = []
        params.append(request.json['id_corrida'])
        params.append(request.json['id_motorista'])
        params.append(request.json['CPF_passageiro'])
        params.append(request.json['avaliacao_condutor'])
        params.append(request.json['avaliacao_veiculo'])
        params.append(request.json['data_inicio'])
        params.append(request.json['data_fim'])
        params.append(request.json['origem'])
        params.append(request.json['destino'])
        params.append(request.json['tarifa'])
        params.append(request.json['distancia'])
        print(params)
        
        try:
            corrida.create(params)
        except Exception as e:
            return str(e), 400
        return 'OK'

    def updateCorrida(self, request):
        params = []
        params.append(request.json['id_corrida'])
        params.append(request.json['id_motorista'])
        params.append(request.json['CPF_passageiro'])
        params.append(request.json['avaliacao_condutor'])
        params.append(request.json['avaliacao_veiculo'])
        params.append(request.json['data_inicio'])
        params.append(request.json['data_fim'])
        params.append(request.json['origem'])
        params.append(request.json['destino'])
        params.append(request.json['tarifa'])
        params.append(request.json['distancia'])
        try:
            corrida = Corrida(params)
            corrida.update()
        except Exception as e:
            return str(e), 400
        return 'OK'
    
    def deleteCorrida(self, request):
        corrida = Corrida()

        try:
            print(request.args.get('idCorrida'))
            corrida.findById(request.args.get('idCorrida'))
            corrida.delete()
            return 'OK'
        except Exception as e:
            return str(e) , 400
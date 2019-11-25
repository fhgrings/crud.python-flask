from ..model.Veiculo import Veiculo


class VeiculoService():
    def getVeiculo(self, request):
        veiculo = Veiculo()
        try:
            veiculo.findById(request.args.get('idVeiculo'))
        except Exception as e:
            return str(e), 400
        return veiculo.__str__()

    def createVeiculo(self, request):
        veiculo = Veiculo()
        params = []
        params.append(request.json['renavan'])
        params.append(request.json['placa'])
        params.append(request.json['id_modelo_veiculo'])

        try:
            veiculo.create(params)
        except Exception as e:
            return str(e), 400
        return 'OK'

    def updateVeiculo(self, request):
        params = []
        params.append(request.json['renavan'])
        params.append(request.json['placa'])
        params.append(request.json['id_modelo_veiculo'])

        try:
            veiculo = Veiculo(params)
            veiculo.update()
        except Exception as e:
            return str(e), 400
        return 'OK'
    
    def deleteVeiculo(self, request):
        veiculo = Veiculo()

        try:
            veiculo.findById(request.args.get('idVeiculo'))
            veiculo.delete()
        except Exception as e:
            return str(e), 400
        return 'OK'

        
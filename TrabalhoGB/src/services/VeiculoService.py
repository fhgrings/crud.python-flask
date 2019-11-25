from ..model.Veiculo import Veiculo


class VeiculoService():
    def getVeiculo(self, request):
        veiculo = Veiculo()
        veiculo.findById(request.args.get('idVeiculo'))
        return veiculo.__str__()

    def createVeiculo(self, request):
        veiculo = Veiculo()
        params = []
        params.append(request.json['__renavan'])
        params.append(request.json['__placa'])
        params.append(request.json['__id_modelo_veiculo'])
        veiculo.create(params)
        return 'OK'

    def updateVeiculo(self, request):
        params = []
        params.append(request.json['__renavan'])
        params.append(request.json['__placa'])
        params.append(request.json['__id_modelo_veiculo'])
        veiculo = Veiculo(params)
        veiculo.update()
        return 'OK'
    
    def deleteVeiculo(self, request):
        veiculo = Veiculo()
        veiculo.findById(request.args.get('idVeiculo'))
        veiculo.delete()
        return 'OK'

        
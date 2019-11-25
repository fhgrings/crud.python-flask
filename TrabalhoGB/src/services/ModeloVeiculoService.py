from ..model.ModeloVeiculo import ModeloVeiculo

class ModeloVeiculoService():
    def getModeloVeiculo(self, request):
        modeloVeiculo = ModeloVeiculo()
        modeloVeiculo.findById(request.args.get('idModeloVeiculo'))
        return modeloVeiculo.__str__()

    def createModeloVeiculo(self, request):
        modeloVeiculo = ModeloVeiculo()
        params = []
        params.append(request.json['id_modelo_Veiculo'])
        params.append(request.json['modelo'])
        params.append(request.json['marca'])
        params.append(request.json['ano'])
        modeloVeiculo.create(params)
        return 'OK'

    def updateModeloVeiculo(self, request):
        params = []
        params.append(request.json['id_modelo_Veiculo'])
        params.append(request.json['modelo'])
        params.append(request.json['marca'])
        params.append(request.json['ano'])
        modeloVeiculo = ModeloVeiculo(params)
        modeloVeiculo.update()
        return 'OK'
    
    def deleteModeloVeiculo(self, request):
        modeloVeiculo = ModeloVeiculo()
        modeloVeiculo.findById(request.args.get('idModeloVeiculo'))
        modeloVeiculo.delete()
        return 'OK'
from ..model.ModeloVeiculo import ModeloVeiculo

class ModeloVeiculoService():
    def getModeloVeiculo(self, request):
        modeloVeiculo = ModeloVeiculo()
        try:
            modeloVeiculo.findById(request.args.get('idModeloVeiculo'))
        except Exception as e:
            return e
        return modeloVeiculo.__str__()

    def createModeloVeiculo(self, request):
        modeloVeiculo = ModeloVeiculo()
        params = []
        params.append(request.json['id_modelo_Veiculo'])
        params.append(request.json['modelo'])
        params.append(request.json['marca'])
        params.append(request.json['ano'])
        
        try:
            modeloVeiculo.create(params)
        except Exception as e:
            return e
        return 'OK'

    def updateModeloVeiculo(self, request):
        params = []
        params.append(request.json['id_modelo_Veiculo'])
        params.append(request.json['modelo'])
        params.append(request.json['marca'])
        params.append(request.json['ano'])

        try:
            modeloVeiculo = ModeloVeiculo(params)
            modeloVeiculo.update()
        except Exception as e:
            return e
        return 'OK'
    
    def deleteModeloVeiculo(self, request):
        modeloVeiculo = ModeloVeiculo()

        try:
            modeloVeiculo.findById(request.args.get('idModeloVeiculo'))
            modeloVeiculo.delete()
        except Exception as e:
            return e
        return 'OK'
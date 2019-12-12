from flask import request, jsonify
import json


from src.services.CondutorService import CondutorService
from src.services.CorridaService import CorridaService
from src.services.ModeloVeiculoService import ModeloVeiculoService
from src.services.MotoristaService import MotoristaService
from src.services.PassageiroSerice import PassageiroService
from src.services.VeiculoService import VeiculoService
from src.services.InformacoesCondutorService import InformacoesCondutorService
from src.services.InformacoesCorridaService import InformacoesCorridaService
from src.services.InformacoesVeiculoService import InformacoesVeiculoService

def configure(app):

    @app.route('/')
    def alive():
        return "Alive"



    @app.route("/condutor/info/")
    def getInfoCondutor():
        condutorService = CondutorService()
        print(condutorService.getInformacoesCondutor())
        return "ok"

    @app.route("/condutor/get/", methods=['GET'])
    def getCondutor():
        try:
            condutorService = CondutorService()
            return condutorService.getCondutor(request)
        except Exception as e:
            return str(e), 500

    @app.route("/condutor/all/", methods=['GET'])
    def getAllCondutor():
        try:
            condutorService = CondutorService()
            return condutorService.getAll(request)
        except Exception as e:
            return str(e), 400


    @app.route("/condutor/create/", methods=['PUT'])
    def createCondutor():
        condutorService = CondutorService()
        return condutorService.createCondutor(request)

    @app.route("/condutor/update/", methods=['POST'])
    def updateCondutor():
        condutorService = CondutorService()
        return condutorService.updateCondutor(request)
    
    @app.route("/condutor/delete/", methods=['DELETE'])
    def deleteCondutor():
        condutorService = CondutorService()
        return condutorService.deleteCondutor(request)





    @app.route("/corrida/get/", methods=['GET'])
    def getCorrida():
        corridaService = CorridaService()
        return corridaService.getCorrida(request)

    @app.route("/corrida/create/", methods=['PUT'])
    def createCorrida():
        corridaService = CorridaService()
        return corridaService.createCorrida(request)

    @app.route("/corrida/update/", methods=['POST'])
    def updateCorrida():
        corridaService = CorridaService()
        return corridaService.updateCorrida(request)
    
    @app.route("/corrida/delete/", methods=['DELETE'])
    def deleteCorrida():
        corridaService = CorridaService()
        return corridaService.deleteCorrida(request)





    @app.route("/modelo-veiculo/get/", methods=['GET'])
    def getModeloVeiculo():
        modeloVeiculoService = ModeloVeiculoService()
        return modeloVeiculoService.getModeloVeiculo(request)

    @app.route("/modelo-veiculo/create/", methods=['PUT'])
    def createModeloVeiculo():
        modeloVeiculoService = ModeloVeiculoService()
        return modeloVeiculoService.createModeloVeiculo(request)

    @app.route("/modelo-veiculo/update/", methods=['POST'])
    def updateModeloVeiculo():
        modeloVeiculoService = ModeloVeiculoService()
        return modeloVeiculoService.updateModeloVeiculo(request)
    
    @app.route("/modelo-veiculo/delete/", methods=['DELETE'])
    def deleteModeloVeiculo():
        modeloVeiculoService = ModeloVeiculoService()
        return modeloVeiculoService.deleteModeloVeiculo(request)
    

    @app.route("/motorista/get/", methods=['GET'])
    def getMotorista():
        motoristaService = MotoristaService()
        return motoristaService.getMotorista(request)

    @app.route("/motorista/create/", methods=['PUT'])
    def createMotorista():
        motoristaService = MotoristaService()
        return motoristaService.createMotorista(request)


    @app.route("/motorista/update/", methods=['POST'])
    def updateMotorista():
        motoristaService = MotoristaService()
        return motoristaService.updateMotorista(request)

    
    @app.route("/motorista/delete/", methods=['DELETE'])
    def deleteMotorista():
        motoristaService = MotoristaService()
        return motoristaService.deleteMotorista(request)


    @app.route("/passageiro/get/", methods=['GET'])
    def getPassageiro():
        passageiroService = PassageiroService()
        return passageiroService.getPassageiro(request)

    @app.route("/passageiro/create/", methods=['PUT'])
    def createPassageiro():
        passageiroService = PassageiroService()
        return passageiroService.createPassageiro(request)

    @app.route("/passageiro/update/", methods=['POST'])
    def updatePassageiro():
        passageiroService = PassageiroService()
        return passageiroService.updatePassageiro(request)
    
    @app.route("/passageiro/delete/", methods=['DELETE'])
    def deletePassageiro():
        passageiroService = PassageiroService()
        return passageiroService.deletePassageiro(request)



    @app.route("/veiculo/get/", methods=['GET'])
    def getVeiculo():
        veiculoService = VeiculoService()
        return veiculoService.getVeiculo(request)

    @app.route("/veiculo/create/", methods=['PUT'])
    def createVeiculo():
        veiculoService = VeiculoService()
        return veiculoService.createVeiculo(request)

    @app.route("/veiculo/update/", methods=['POST'])
    def updateVeiculo():
        veiculoService = VeiculoService()
        return veiculoService.updateVeiculo(request)
    
    @app.route("/veiculo/delete/", methods=['DELETE'])
    def deleteVeiculo():
        veiculoService = VeiculoService()
        return veiculoService.deleteVeiculo(request)


    @app.route("/informacoesCorrida/all/", methods=['GET'])
    def getInformacoesCorrida():
        informacoesCorridaService = InformacoesCorridaService()
        return informacoesCorridaService.getAll(request)

    @app.route("/informacoesCondutor/all/", methods=['GET'])
    def Passageiro():
        informacoesCondutorService = InformacoesCondutorService()
        return informacoesCondutorService.getAll(request)

    @app.route("/informacoesCondutor/get/", methods=['GET'])
    def getInformacoesCondutor():
        informacoesCondutorService = InformacoesCondutorService()
        return informacoesCondutorService.getOne(request)

    @app.route("/informcoesVeiculo/all/", methods=['GET'])
    def getInformacoesVeiculo():
        informacoesVeiculoService = InformacoesVeiculoService()
        return informacoesVeiculoService.getAll(request)
        
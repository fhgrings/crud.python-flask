from .Database import Database
from datetime import datetime

class HyberGrings():

    def childClassStringify(self, childDictKeys):
        for rawAttribute in childDictKeys:
            self.childAttributeList.append(rawAttribute)
            nameAttributeVector = rawAttribute.split("_")[3:]
            if nameAttributeVector != []:
                self.queryParamsList.append('_'.join(nameAttributeVector))

    def __init__(self, tableName, childDict, primaryKeys = 1):
        self.query = None
        self.childAttributeList = []
        self.queryParamsList = []
        self.table = str(tableName)
        self.primaryKeys = primaryKeys

        database = Database()
        self.banco, self.cursor = database.connectionFactory()

        self.childDict = childDict
        self.childClassStringify(childDict.keys())
            
    
    def update(self):
        self.query = "UPDATE "
        self.query += self.table
        self.query += " SET "
        print(self.queryParamsList)
        for index in range(1,len(self.queryParamsList) - 1):
            self.query += self.queryParamsList[index]
            self.query += " = "
            self.query += "'" + str(self.childDict[self.childAttributeList[index]]) + "', "
        self.query = self.query[:-2]
        self.query += " WHERE ( "
        for index in range(self.primaryKeys):
            self.query += self.queryParamsList[index] + " = " + str(self.childDict[self.childAttributeList[index]]) + " AND "
        self.query = self.query[:-4] 
        self.query += " )"

        print("QUERY:\n\n" + self.query + "\n\n")

        try:
            self.cursor.execute(self.query)
            self.banco.commit()
        except Exception as e:
            raise Exception (e)
        return self.cursor.rowcount

    def findAll(self):
        self.query = "SELECT * FROM " + self.table
        print(self.query)
        self.cursor.execute(self.query)
        teste = self.childDict.__init__
        print(teste)
        return self.cursor.fetchall()


    def findById(self, id):
        if(type(id) == int):
            id = str(id)
        
        self.query = "SELECT * FROM "
        self.query += self.table
        self.query += " WHERE "
        self.query += self.queryParamsList[0]
        self.query += " = " + id

        print(self.query)
        self.cursor.execute(self.query)
        resultado = self.cursor.fetchone()
        if resultado is None:
            raise Exception ("Id nao encontrado") 

        self.fromTuple(resultado)
        print(self.query)

    def create(self, params):
        print(params)
        print(self.queryParamsList)
        if len(params) != len(self.queryParamsList):
            raise Exception("Quantidade de informações incorreta.")

        self.query = "INSERT INTO "
        self.query += self.table
        self.query += " ( "
        for index in range(0,len(self.queryParamsList)):
            self.query +=  self.queryParamsList[index]
            self.query += ","
        self.query = self.query[:-1]
        self.query += " ) "
        self.query += " VALUES ( "
        for param in params:
            self.query += "'" + str(param) + "'"
            self.query += ","
        self.query = self.query[:-1]
        self.query += " ) "

        print(self.query)

        try:
            self.cursor.execute(self.query)
            self.banco.commit()
        except Exception as e:
            raise Exception (e)
        # self.childDict[self.childAttributeList[0]] = self.cursor.lastrowid
        print("Passei")
        self.loadObject(params)


    def loadObject(self, params):
        for index in range(0,len(self.queryParamsList) -1):
            self.childDict[self.childAttributeList[index]] = params[index]

    def delete(self):
        self.query = "DELETE FROM "
        self.query += self.table
        self.query += " WHERE ( "
        for index in range(self.primaryKeys):
            self.query += self.queryParamsList[index] + " = " + str(self.childDict[self.childAttributeList[index]]) + " AND "
        self.query = self.query[:-4]
        self.query += ")"

        print(self.query)
        try:
            self.cursor.execute(self.query)
            self.banco.commit()
        except Exception as e:
            return str(e)

    def toTuple(self):
        retorno = []
        for param in self.childAttributeList:
            retorno.append(self.childDict[param])
        return retorno

    def fromTuple(self,dados):
        for index in range(0,len(dados)):
            self.childDict[self.childAttributeList[index]] = dados[index]
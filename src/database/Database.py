import mysql.connector


class Database:
    connection = False
    banco = None
    cursor = None

    def connectionFactory(self):
        if self.connection :
            return self.banco, self.cursor
        else:
            self.banco = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                passwd = "",
                database = "MeLeva"
            )
            self.cursor = self.banco.cursor()
            self.connection = True

        return  self.banco, self.cursor
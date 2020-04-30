import mysql.connector


class ConnectionDataBase:

    def open_connection(self):
        try:
            connection = mysql.connector.connect(user="root",
                                                 password="",
                                                 host="localhost",
                                                 database="BD_AGENDA")

            cursor = connection.cursor()
            self.connection = connection
            self.cursor = cursor
            print("Conexão Aberta.")

        except mysql.Error:
            print("Erro ao tentar realizar a conexão com o Banco de Dados BD_AGENDA.")
            self.close_connection()
        except():
            print("Erro em geral ao tentar realizar a conexão com o Banco de Dados.")
            self.close_connection()

    def close_connection(self):
        try:
            if self.connection.is_connected():
                self.connection.close()
                print("Conexão Fechada.")
        except():
            print("Erro ao tentar fechar a conexão com o Banco de Dados.")



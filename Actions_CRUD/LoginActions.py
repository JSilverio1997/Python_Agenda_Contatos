import mysql
from Database.ConnectionDatabase import ConnectionDataBase
import tkinter.messagebox


class Login(ConnectionDataBase):

    def check_login(self, nickname):
        try:
            self.open_connection()
            sql = f"select id_login from login where upper(nickname) = '{nickname.upper()}';"
            self.cursor.execute(sql)
            id_login = self.cursor.fetchone()

            if id_login is not None:
                return id_login[0]
            else:
                return None

        except():
            print("_" * 80)
            tkinter.messagebox.showerror("Erro", "Erro ao tentar checar se o Login existe ou não")
        finally:
            self.close_connection()

    def check_login_activate(self, id_login):
        try:
            self.open_connection()
            sql = f"select login_ativo from login where id_login = {id_login};"
            self.cursor.execute(sql)
            login_activity = self.cursor.fetchone()
            if login_activity is not None:
                return login_activity[0]
            else:
                return None

        except():
            tkinter.messagebox.showerror("Error", "Erro ao tentar verificar se o login está ativo ou não")
        finally:
            self.close_connection()

    def return_nickname(self, id_login):
        try:
            self.open_connection()
            sql = f"select nickname from login where id_login = {id_login};"
            self.cursor.execute(sql)
            nickname = self.cursor.fetchone()

            if nickname is not None:
                return nickname[0]
            else:
                return None

        except():
            print("_" * 80)
            tkinter.messagebox.showerror("Erro", "Erro ao tentar retornar o nickname.")
        finally:
            self.close_connection()

    def return_question(self, nickname):
        try:
            id_login = self.check_login(nickname)
            if id_login is not None:
                self.open_connection()
                sql = f"select pergunta from login where id_login = {id_login};"
                self.cursor.execute(sql)
                question = self.cursor.fetchone()
                if question is not None:
                    return f" Responda a pergunta abaixo.\n {question[0].replace('?', '')} ? "
                else:
                    return None
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar checar a pergunta.")
        finally:
            self.close_connection()

    def recover_password(self, nickname, answer):
        try:
            id_login = self.check_login(nickname)
            if id_login is not None:
                self.open_connection()
                sql = f"select senha from login where id_login = {id_login} and resposta = '{answer}';"
                self.cursor.execute(sql)
                password = self.cursor.fetchone()
                if password is not None:
                    return f"A sua senha é: {password[0]}"
                else:
                    return None
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar checar a pergunta.")
        finally:
            self.close_connection()

    def return_datas_login(self, id_login):
        try:
            self.open_connection()
            sql = f"select nome, nickname, senha, pergunta, resposta from login where id_login = {id_login};"
            self.cursor.execute(sql)
            datas_login = self.cursor.fetchone()
            if datas_login is not None:
                return datas_login
            else:
                return None

        except():
            tkinter.messagebox.showwarning("Atenção", "Erro ao tentar retornar os dados do Login.")
        finally:
            self.close_connection()

    def insert(self, datas={}):
        try:
            check_login = self.check_login(datas['nickname'])
            if check_login is None:
                self.open_connection()
                sql = f"insert into login(nome, nickname, senha, pergunta, resposta) " \
                      f"values('{datas['nome']}', '{datas['nickname']}', " \
                      f"'{datas['senha']}', '{datas['pergunta']}', '{datas['resposta']}');"
                self.cursor.execute(sql)
                self.connection.commit()
                status_create = "created"
                return status_create
            else:
                return None

        except mysql.connector.errors.IntegrityError:
            tkinter.messagebox.showwarning("Atenção", "Erro na integridade das informações.")
        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar cadastrar o login.")
        finally:
            self.close_connection()

    def update(self, datas={}):
        try:
            self.open_connection()
            sql = f"update login " \
                  f"set senha = '{datas['senha']}'" \
                  f"   ,pergunta = '{datas['pergunta']}'" \
                  f"   ,resposta = '{datas['resposta']}' "\
                  f"where id_login = {datas['id_login']}" \
                  f" and login_ativo = 'Y';"

            self.cursor.execute(sql)
            self.connection.commit()
            return "Os dados do usuário foi alterado."

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar realizar a atualização da senha.")
        finally:
            self.close_connection()

    def deactivate_login(self, id_login, desactive_flag):
        try:
            recovered_nickame = self.return_nickname(id_login)

            if recovered_nickame is not None:
                if desactive_flag == 'N':
                    self.open_connection()
                    sql = f"update login " \
                          f"set login_ativo = 'N'"\
                          f" where id_login = {id_login};"

                    self.cursor.execute(sql)
                    self.connection.commit()
                    return "Desativado"
                else:
                    self.open_connection()
                    sql = f"update login " \
                          f"set login_ativo = 'Y'"\
                          f" where id_login = {id_login};"

                    self.cursor.execute(sql)
                    self.connection.commit()
                    return "Ativado"
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar Desativar ou Ativar o Login.")
        finally:
            self.close_connection()

    def logar(self, nickname, senha):
        try:
            self.open_connection()
            sql = f"select id_login from login where nickname = '{nickname}' and senha = '{senha}' ;"
            self.cursor.execute(sql)
            id_login = self.cursor.fetchone()

            if id_login is not None:
                return id_login[0]
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar logar no sistema.")
        finally:
            self.close_connection()

    def delete(self, id_login):
        try:
            nickname = self.return_nickname(id_login)

            if nickname is not None:
                self.open_connection()
                sql = f"delete from login where id_login = {id_login};"
                self.cursor.execute(sql)
                self.connection.commit()
                return f"O Login foi excluído."

            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", " Erro ao tentar excluír o registro.")
        finally:
            self.close_connection()


"""dados = {"id_login": 4, "nome": "Tester", "nickname": "Teste 2",
         "senha": "abcd", "pergunta": "teste", "resposta": "teste"}"""
# login = Login()
# print(login.insert(dados))
# print(login.update(dados))
# print(login.logar(dados['nickname'], dados['senha']))
# print(login.check_login(dados['nickname']))
# print(login.return_question(dados['nickname']))
# print(login.recover_password(dados['nickname'], dados['resposta']))
# print(login.delete(dados['nickname']))

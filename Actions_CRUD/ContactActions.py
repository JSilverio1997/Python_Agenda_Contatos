import tkinter.messagebox
import mysql
from Database.ConnectionDatabase import ConnectionDataBase


class Contact(ConnectionDataBase):

    def check_contact(self, id_login, name):
        try:
            self.open_connection()
            sql = f"select id_contato from contatos where upper(nome) = '{name.upper()}' and id_login = {id_login};"
            self.cursor.execute(sql)
            id_contato = self.cursor.fetchone()

            if id_contato is not None:
                return id_contato[0]
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar realizar a consulta de checagem de contato.")
        finally:
            self.close_connection()

    def insert(self, contact={}):
        try:
            check_contact = self.check_contact(contact['id_login'], contact['nome'])

            if check_contact is None:
                self.open_connection()
                sql = f"insert into contatos(id_login, nome, numero_principal, numero_secundario) values(" \
                      f"{contact['id_login']}, '{contact['nome']}', '{contact['numero_principal']}', " \
                      f"'{contact['numero_secundario']}');"
                self.cursor.execute(sql)
                self.connection.commit()
                return "Cadastrado com Sucesso."
            else:
                return None

        except mysql.connector.errors.IntegrityError:
            tkinter.messagebox.showerror("Erro", "Erro Não Existe Este Login Cadastrado.")
            exit()
        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar cadastrar o contato.")
        finally:
            self.close_connection()

    def update(self, contact={}):
        try:
            id_contato = self.check_contact(contact['id_login'], contact['nome_recuperado'])

            if id_contato is not None:

                avaible_name = self.check_contact(contact['id_login'], contact['nome'])

                if avaible_name is None:
                    self.open_connection()
                    sql = "update contatos" \
                          f" set nome = '{contact['nome']}'" \
                          f" where id_contato = {id_contato};"
                    self.cursor.execute(sql)
                    self.connection.commit()
                    self.close_connection()
                else:
                    tkinter.messagebox.showwarning("Atenção", "Este nome já esta sendo usado nao vai atualizar o nome.")

                self.open_connection()
                sql = "update contatos" \
                      f" set numero_principal = '{contact['numero_principal']}'" \
                      f"    ,numero_secundario = '{contact['numero_secundario']}' " \
                      f" where id_contato = {id_contato};"
                self.cursor.execute(sql)
                self.connection.commit()

                return "Os dados deste contato foram atualizados."
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar realizar a atualização dos dados do contato.")
        finally:
            self.close_connection()

    def search_contact(self, id_login, name):
        try:
            self.open_connection()
            sql = f"select nome, numero_principal, numero_secundario from contatos__desc_v " \
                  f"where upper(nome) like '%{name.upper()}%' and id_login = {id_login};"
            self.cursor.execute(sql)
            contact = self.cursor.fetchone()

            if contact is not None:
                return contact
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar pesquisar este usuário na sua lista.")
        finally:
            self.close_connection()

    def show_contact(self, id_login):
        try:
            self.open_connection()
            sql = f"select nome, numero_principal, numero_secundario " \
                  f"from contatos__desc_v where id_login = {id_login} order by nome limit 10;"
            self.cursor.execute(sql)
            contacts = self.cursor.fetchall()

            if contacts is not None:
                return contacts
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar consultar os contatos da lista.")
        finally:
            self.close_connection()

    def delete(self, id_login, name):
        try:
            id_contato = self.check_contact(id_login, name)

            if id_contato is not None:
                self.open_connection()
                sql = f"delete from contatos where id_contato = {id_contato};"
                self.cursor.execute(sql)
                self.connection.commit()
                return "O Contato foi excluído com Sucesso."
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar excluir o contato.")
        finally:
            self.close_connection()


"""dados = {"id_login": 3, "nome_recuperado": "Osvaldo", "nome": "Karoline", "numero_principal": "119987-9288",
         "numero_secundario": "NULL"}"""
# contato = Contact()
# print(contato.check_contact(dados['id_login'], dados['nome']))
# print(contato.insert(dados))
# print(contato.update(dados))
# print(contato.search_contact(dados['id_login'], dados['nome_pesquisado']))
# print(contato.show_contact(dados['id_login']))
# print(contato.delete(dados['id_login'], dados['nome']))

import tkinter.messagebox
from Database.ConnectionDatabase import ConnectionDataBase


class ContactHistoric(ConnectionDataBase):

    def search_contact_historic(self, id_login, name):
        try:
            self.open_connection()
            sql = f"select nome, numero_principal, numero_secundario, status_contato, data_criacao, data_alteracao" \
                  f" from HISTORICO_CONTATOS_DESC_V where upper(nome) like '%{name.upper()}%' " \
                  f" and id_login = {id_login};"
            self.cursor.execute(sql)
            historic = self.cursor.fetchone()

            if historic is not None:
                return historic
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar pesquisar o contato no histórico.")
        finally:
            self.close_connection()

    def show_contact_historic(self, id_login):
        try:
            self.open_connection()
            sql = f"select nome, numero_principal, numero_secundario, status_contato, data_criacao, data_alteracao" \
                  f" from HISTORICO_CONTATOS_DESC_V where id_login = {id_login} order by status_contato limit 10;"
            self.cursor.execute(sql)
            historic = self.cursor.fetchall()

            if historic is not None:
                return historic
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar consultar o histórico de contatos do login.")
        finally:
            self.close_connection()


# historic_contact = ContactHistoric()
# print(historic_contact.search_contact_historic(1, 'Ma'))
# print(historic_contact.show_contact_historic(3))

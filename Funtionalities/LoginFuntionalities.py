import tkinter.messagebox
from Getters_Setters.LoginGetSetter import LoginGetSetter
from Actions_CRUD.LoginActions import Login


class LoginFuntionalities(LoginGetSetter):

    def logar(self, nickname, password):
        try:
            login_actions = Login()

            LoginGetSetter.nickname = nickname
            LoginGetSetter.password = password

            id_login = login_actions.logar(LoginGetSetter.nickname, LoginGetSetter.password)
            if id_login is not None:
                tkinter.messagebox.showinfo("Login", "Logado com sucesso.")
                login_activity = login_actions.check_login_activate(id_login)
                datas_return_login = {'login_ativo': login_activity, 'id_login': id_login}

                if login_activity == "Y":
                    return datas_return_login
                else:
                    if tkinter.messagebox.askyesnocancel("Ativar", "Deseja Ativar o seu Login : "):
                        self.deactivate_login(id_login, 'Y')
                    else:
                        login_actions.close_connection()

                    return datas_return_login
            else:
                datas_return_login = {'login_ativo': 'N', 'id_login': None}
                tkinter.messagebox.showwarning("Atenção", "Login Incorreto verifique o seu nickname ou senha.")
                return datas_return_login

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar logar. ")
            raise

    @staticmethod
    def create_login(list_datas=[]):
        try:
            dict_login = {}

            LoginGetSetter.name = list_datas[0]
            LoginGetSetter.nickname = list_datas[1]
            LoginGetSetter.password = list_datas[2]
            LoginGetSetter.question = list_datas[4]
            LoginGetSetter.answer = list_datas[5]

            dict_login['nome'] = LoginGetSetter.name
            dict_login['nickname'] = LoginGetSetter.nickname
            dict_login['senha'] = LoginGetSetter.password
            dict_login['pergunta'] = LoginGetSetter.question
            dict_login['resposta'] = LoginGetSetter.answer

            insert_login = Login()
            created_login = insert_login.insert(dict_login)
            if created_login is not None:
                return created_login
            else:
                return None

        except():
            tkinter.messagebox.showwarning("Atenção", "Erro ao tentar cadastrar este login.")
            raise

    @staticmethod
    def return_question(nickname):
        try:
            login = Login()
            question = login.return_question(nickname)
            if question is not None:
                return question
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar recuperar a pergunta.")

    @staticmethod
    def recover_password(nickname, answer):
        login = Login()
        recover_pwd = login.recover_password(nickname, answer)
        if recover_pwd is not None:
            return recover_pwd
        else:
            return None

    @staticmethod
    def return_datas_login(id_login):
        dict_datas_login = {}
        login = Login()
        datas_login = login.return_datas_login(id_login)
        if datas_login is not None:
            dict_datas_login['name'] = datas_login[0]
            dict_datas_login['nickname'] = datas_login[1]
            dict_datas_login['password'] = datas_login[2]
            dict_datas_login['question'] = datas_login[3]
            dict_datas_login['answer'] = datas_login[4]

            return dict_datas_login
        else:
            return None

    @staticmethod
    def update_datas_login(id_login, list_datas=[]):
        try:
            dict_data = {}
            LoginGetSetter.id_login = id_login
            LoginGetSetter.password = list_datas[0]
            LoginGetSetter.question = list_datas[1]
            LoginGetSetter.answer = list_datas[2]

            dict_data['id_login'] = LoginFuntionalities.id_login
            dict_data['senha'] = LoginGetSetter.password
            dict_data['pergunta'] = LoginGetSetter.question
            dict_data['resposta'] = LoginGetSetter.answer

            login = Login()
            updated_datas = login.update(dict_data)
            if updated_datas is not None:
                return updated_datas

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar atualizar os dados do Login.")
            raise

    @staticmethod
    def deactivate_login(id_login, desactive_flag):
        try:
            LoginGetSetter.id_login = id_login
            LoginGetSetter.desactive_flag = desactive_flag

            login = Login()
            login_desactive = login.deactivate_login(LoginGetSetter.id_login, LoginGetSetter.desactive_flag)
            if login_desactive == "Ativado":
                tkinter.messagebox.showinfo("OK", "O Login está ativado.")
                return login_desactive

            elif login_desactive == "Desativado":
                tkinter.messagebox.showinfo("OK", "O Login está desativado.")
                return login_desactive

            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar Ativar ou Desativar o login.")
            raise

    @staticmethod
    def delete_login(id_login):
        try:
            if id_login is not None:
                LoginGetSetter.id_login = id_login
                login = Login()
                login_deleted = login.delete(LoginGetSetter.id_login)
                if login_deleted is not None:
                    return login_deleted
                else:
                    return None

        except():
            tkinter.messagebox.showwarning("Atenção", "Erro ao tentar excluir o Login.")
            raise


"""name = "Teste aplicacao"
nickname = "test 1"
password = "ssss"
confirm_password = "ssss"
question = "abcd"
answer = "defg"
"""
# datas_test = [name, nickname, password, confirm_password, question, answer]
# datas_test = [password, question, answer]
# print(datas_test)
# login_test = LoginFuntionalities()
# login_test.logar("user_tester", "12345")
# login_test.logar(datas_test[1], datas_test[2])
# print(login_test.create_login(datas_test))
# return_question = login_test.return_question(datas_test[1])
# print(return_question)
# recover_pwd = login_test.recover_password(datas_test[1], datas_test[5])
# print(recover_pwd)
# login_test.update_datas_login(10, datas_test)
# login_test.deactivate_login(12, "N")
# login_test.delete_login(11)

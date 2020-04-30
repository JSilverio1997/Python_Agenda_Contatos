import tkinter.messagebox
from tkinter import *
from Funtionalities.LoginFuntionalities import LoginFuntionalities
from Graphic_Interfaces.FormMainMenu import FormMenu


class FormOptionsLogin(FormMenu):

    def __init__(self, master, id_login):
        self.master = master
        self.master.title("Opções")
        self.create_comp_form_options_login(master)
        self.id_login = id_login
        self.return_datas_login()

    def create_comp_form_options_login(self, window):
        self.create_menu_component(window)

        lbl_nome = Label(text="Opções-Login", font="arial, 18", bg="light gray")
        lbl_nome.grid(row=1, column=4, columnspan=1, pady=5)

        canvas_image = Canvas(window, width=225, height=220)
        bg_image = tkinter.PhotoImage(file=r"Images/Options.png")
        canvas_image.create_image((0, 0), image=bg_image, anchor=NW)
        canvas_image.image = bg_image
        canvas_image.grid(row=2, column=4, columnspan=1, pady=5)

        lbl_nome = Label(text="        Nome: ", font="arial, 14", bg="light gray")
        lbl_nome.grid(row=4, column=3, columnspan=1, pady=5)

        txt_nome = Entry(font="arial,12", width=30)
        txt_nome.grid(row=4, column=4, columnspan=1)
        txt_nome.focus()
        self.txt_nome = txt_nome

        lbl_nickname = Label(text="  Nickname: ", font="arial, 14", bg="light gray")
        lbl_nickname.grid(row=5, column=3, columnspan=1, pady=5)

        txt_nickname = Entry(font="arial,12", width=30)
        txt_nickname.grid(row=5, column=4, columnspan=1)
        self.txt_nickname = txt_nickname

        lbl_password = Label(text="        Senha: ", font="arial, 14", bg="light gray")
        lbl_password.grid(row=6, column=3, columnspan=1, pady=5)

        txt_password = Entry(font="arial,12", width=30, show="*")
        txt_password.grid(row=6, column=4, columnspan=1)
        self.txt_password = txt_password

        lbl_question = Label(text="   Pergunta: ", font="arial, 14", bg="light gray")
        lbl_question.grid(row=7, column=3, columnspan=1, pady=5)

        txt_question = Entry(font="arial,12", width=30)
        txt_question.grid(row=7, column=4, columnspan=1)
        self.txt_question = txt_question

        lbl_answer = Label(text="   Resposta: ", font="arial, 14", bg="light gray")
        lbl_answer.grid(row=8, column=3, columnspan=1, pady=5)

        txt_answer = Entry(font="arial,12", width=30)
        txt_answer.grid(row=8, column=4, columnspan=1)
        self.txt_answer = txt_answer

        # Buttons
        btn_alterar = Button(text="Alterar", width=20, font="Arial", command=self.update_datas_login)
        btn_alterar.grid(row=10, column=4, columnspan=2, padx=15, pady=5)

        btn_deletar = Button(text="Excluir", width=20, font="Arial", command=self.delete)
        btn_deletar.grid(row=11, column=4, columnspan=2, padx=15, pady=5)

        btn_limpar = Button(text="Limpar", width=20, font="Arial", command=self.clear)
        btn_limpar.grid(row=12, column=4, columnspan=20, padx=15, pady=5)

        btn_voltar = Button(text="Voltar", width=20, font="Arial", command=self.return_form_menu)
        btn_voltar.grid(row=13, column=4, columnspan=20, padx=15, pady=5)

    def return_datas_login(self):
        functions_login = LoginFuntionalities()
        datas_login = functions_login.return_datas_login(self.id_login)

        if datas_login is not None:
            self.txt_nome.insert(1, datas_login['name'])
            self.txt_nome.configure(state="read")
            self.txt_nickname.insert(2, datas_login['nickname'])
            self.txt_nickname.configure(state="read")
            self.txt_password.insert(3, datas_login['password'])
            self.txt_question.insert(3, datas_login['question'])
            self.txt_answer.insert(4, datas_login['answer'])

    def update_datas_login(self):
        password = self.txt_password.get()
        question = self.txt_question.get()
        answer = self.txt_answer.get()

        if password.strip(" ") == "" or len(password.strip(" ")) < 4:
            tkinter.messagebox.showwarning("Atenção", "A senha está inválida para ser alterada, digite novamente.")
            self.txt_password.focus()

        elif password == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor não deixe o campo em branco.")
            self.txt_password.focus()

        elif question.strip(" ") == "" or len(question.strip(" ")) <= 3:
            tkinter.messagebox.showwarning("Atenção", "A pergunta está inválida para ser alterada.")
            self.txt_question.focus()

        elif question == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite uma pergunta.")
            self.txt_question.focus()

        elif answer.strip(" ") == "" or len(answer.strip(" ")) <= 3:
            tkinter.messagebox.showwarning("Atenção", "A resposta está inválida para ser alterada.")
            self.txt_answer.focus()

        elif answer == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite uma resposta.")
            self.txt_password.focus()

        else:
            if tkinter.messagebox.askyesnocancel("Alterar Dados", "Você realmente deseja alterar os seus dados ?"):
                login = LoginFuntionalities()
                datas_login = [self.txt_password.get(), self.txt_question.get(), self.txt_answer.get()]

                update_datas_login = login.update_datas_login(self.id_login, datas_login)
                if update_datas_login is not None:
                    tkinter.messagebox.showinfo("Ok", "Os dados foram alterados com sucesso.")

    def delete(self):

        if tkinter.messagebox.askyesnocancel("Excluir", "Você deseja excluir o seu Login ?"):
            login = LoginFuntionalities()
            login_deleted = login.delete_login(self.id_login)
            if login_deleted is not None:
                tkinter.messagebox.showinfo("OK", "O Login foi excluído com sucesso.")
                self.master.destroy()
                from Graphic_Interfaces.FormLogin import instance_form_login
                instance_form_login()

    def clear(self):
        self.txt_password.delete(0, len(self.txt_password.get()))
        self.txt_question.delete(0, len(self.txt_question.get()))
        self.txt_answer.delete(0, len(self.txt_answer.get()))
        self.txt_password.focus()


def instance_form_options_login(id_login):
    form_options_login = Tk()
    FormOptionsLogin(form_options_login, id_login)
    form_options_login.iconbitmap(r"Images/IconeAgenda.ico")
    form_options_login.configure(relief="ridge", bg="light gray", border="4")
    form_options_login.geometry("420x650+480+2")
    form_options_login.resizable(0, 0)
    form_options_login.mainloop()
    exit()


# instance_form_optiona_login()
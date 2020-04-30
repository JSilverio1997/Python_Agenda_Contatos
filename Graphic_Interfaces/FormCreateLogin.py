from tkinter import *
import tkinter.messagebox
from Funtionalities.LoginFuntionalities import LoginFuntionalities


class FormCriarLogin:

    def __init__(self, master):
        self.master = master
        self.master.title("Criar login")
        self.create_comp_form_create_login(master)

    def create_comp_form_create_login(self, window):
        lbl_title = Label(text="Criar-Login", font="arial, 22", bg="light gray")
        lbl_title.grid(row=1, column=3, pady=10)

        canvas_image = Canvas(window, width=220, height=200)
        bg_image = tkinter.PhotoImage(file=r"Images/Contact.png")
        canvas_image.create_image((0, 0), image=bg_image, anchor=NW)
        canvas_image.image = bg_image
        canvas_image.grid(row=4, column=3, columnspan=1, padx=1, pady=2)

        lbl_name = Label(text="\t    Nome:", font="arial, 14", bg="light gray")
        lbl_name.grid(row=6, column=2, pady=2)

        lbl_nickname = Label(text="               " + "Nickname:", font="arial, 14", bg="light gray")
        lbl_nickname.grid(row=8, column=2, pady=2)

        lbl_password = Label(text="\t  Senha:", font="arial, 14", bg="light gray")
        lbl_password.grid(row=10, column=2, pady=2)

        lbl_confirm_password = Label(text="  Confirmar Senha:", font="arial, 14", bg="light gray")
        lbl_confirm_password.grid(row=12, column=2, pady=2)

        lbl_question = Label(text="               " + "Pergunta:", font="arial, 14", bg="light gray")
        lbl_question.grid(row=14, column=2, pady=2)

        lbl_answer = Label(text="              Resposta:", font="arial, 14", bg="light gray")
        lbl_answer.grid(row=16, column=2, pady=2)

        txt_name = Entry(width="25", font="arial")
        txt_name.grid(row=6, column=3, pady=2)
        txt_name.focus()
        self.txt_name = txt_name

        txt_nickname = Entry(width="25", font="arial")
        txt_nickname.grid(row=8, column=3, pady=2)
        txt_nickname.focus()
        self.txt_nickname = txt_nickname

        txt_password = Entry(width="25", font="arial,12bold", show="*")
        txt_password.grid(row=10, column=3, pady=2)
        self.txt_password = txt_password

        txt_confirm_password = Entry(width="25", font="arial,12bold", show="*")
        txt_confirm_password.grid(row=12, column=3, pady=2)
        self.txt_confirm_password = txt_confirm_password

        txt_question = Entry(width="25", font="arial,12bold")
        txt_question.grid(row=14, column=3, pady=2)
        self.txt_question = txt_question

        txt_answer = Entry(width="25", font="arial,12bold")
        txt_answer.grid(row=16, column=3, pady=2)
        self.txt_answer = txt_answer

        btn_create_login = Button(text="Criar Login", width="18", font="arial", command=self.create_login)
        btn_create_login.grid(row=18, column=3, columnspan=2, padx=3, pady=5)

        btn_clear = Button(text="Limpar", width="18", font="arial", command=self.clear)
        btn_clear.grid(row=19, column=3, columnspan=2, padx=3, pady=5)

        btn_return = Button(text="Voltar", width="18", font="arial", command=self.return_form_login)
        btn_return.grid(row=20, column=3, columnspan=2, padx=3, pady=5)

    def create_login(self):
        name = self.txt_name.get()
        nickname = self.txt_nickname.get()
        password = self.txt_password.get()
        confirm_password = self.txt_confirm_password.get()
        question = self.txt_question.get()
        answer = self.txt_answer.get()

        if name == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite o seu nome.")
            self.txt_name.focus()

        elif nickname == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite o seu Nickname corretamente.")
            self.txt_nickname.focus()

        elif len(nickname.strip(" ")) < 3:
            tkinter.messagebox.showwarning("Atenção", "O Nickname deve ter mais do que 3 caracteres.")
            self.txt_nickname.focus()

        elif password == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite uma senha.")
            self.txt_password.focus()

        elif len(password.strip(" ")) < 4:
            tkinter.messagebox.showwarning("Atenção", "A senha têm que ter mais do que 4 caracteres.")
            self.txt_password.focus()

        elif confirm_password == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor confirme a sua senha.")
            self.txt_confirm_password.focus()

        elif len(confirm_password.strip(" ")) < 4:
            tkinter.messagebox.showwarning("Atenção", "A senha precisa ter mais do que 3 caracteres.")
            self.txt_confirm_password.focus()

        elif password != confirm_password:
            tkinter.messagebox.showwarning("Atenção", "As senhas não se coincidem, por favor digite novamente.")
            self.txt_password.delete(0, len(self.txt_password.get()))
            self.txt_confirm_password.delete(0, len(self.txt_confirm_password.get()))
            self.txt_password.focus()

        elif question == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite a sua pergunta.")
            self.txt_question.focus()

        elif answer == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite uma resposta.")
            self.txt_answer.focus()

        else:
            datas_login = [name, nickname, password, confirm_password, question, answer]
            create_login = LoginFuntionalities()
            created_login = create_login.create_login(datas_login)
            if created_login is not None:
                tkinter.messagebox.showinfo("Sucesso", f"Login foi criado com sucesso.")
                self.clear()
            else:
                tkinter.messagebox.showwarning("Atenção", f" Não foi possível criar o Login, pois ele já existe.")

    def clear(self):
        self.txt_name.delete(0, len(self.txt_name.get()))
        self.txt_nickname.delete(0, len(self.txt_nickname.get()))
        self.txt_password.delete(0, len(self.txt_password.get()))
        self.txt_confirm_password.delete(0, len(self.txt_confirm_password.get()))
        self.txt_question.delete(0, len(self.txt_question.get()))
        self.txt_answer.delete(0, len(self.txt_answer.get()))
        self.txt_name.focus()

    def return_form_login(self):
        self.master.destroy()
        from Graphic_Interfaces.FormLogin import instance_form_login
        instance_form_login()


def instance_form_create_login():
    form_create_login = Tk()
    FormCriarLogin(form_create_login)
    form_create_login.iconbitmap(r"Images/IconeAgenda.ico")
    form_create_login.configure(relief="ridge", bg="light gray", border="4")
    form_create_login.geometry("520x600+470+50")
    form_create_login.resizable(0, 0)
    form_create_login.mainloop()
    exit()


# instance_form_create_login()

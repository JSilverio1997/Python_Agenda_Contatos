import tkinter.messagebox
from tkinter import *
from Funtionalities.LoginFuntionalities import LoginFuntionalities


class FormLogin:

    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.create_comp_form_login(master)

    def create_comp_form_login(self, window):

        lbl_title = Label(text="Login - Agenda", font="arial, 18", bg="light gray")
        lbl_title.grid(row=1, column=3, pady=10)

        canvas_image = Canvas(window, width=200, height=200)
        bg_image = tkinter.PhotoImage(file=r"Images/Contact.png")
        canvas_image.create_image((0, 0), image=bg_image, anchor=NW)
        canvas_image.image = bg_image
        canvas_image.grid(row=4, column=3, columnspan=1, padx=1, pady=4)

        lbl_nickname = Label(text="Nickname:", font="arial, 14", bg="light gray")
        lbl_nickname.grid(row=6, column=2, pady=2)

        lbl_password = Label(text="      Senha:", font="arial, 14", bg="light gray")
        lbl_password.grid(row=8, column=2, pady=2)

        txt_nickname = Entry(width="25", font="arial")
        txt_nickname.grid(row=6, column=3, pady=2)
        txt_nickname.focus()
        self.nickname = txt_nickname

        txt_password = Entry(width="25", font="arial,12bold", show="*")
        txt_password.grid(row=8, column=3, pady=2)
        self.password = txt_password

        btn_forget_password = Button(text="Recuperar Senha", width="20", font="arial,12bold",
                                     command=self.recover_passord)
        btn_forget_password.grid(row=10, column=3, columnspan=2, pady=10)

        btn_login = Button(text="Logar", width="20", font="arial,12bold", command=self.logar_user)
        btn_login.grid(row=15, column=3, columnspan=2, padx=3, pady=10)

        btn_create_login = Button(text="Criar Login", width="20", font="arial", command=self.create_login)
        btn_create_login.grid(row=16, column=3, columnspan=2, padx=3, pady=10)

        btn_clear = Button(text="Limpar", width="20", font="arial", command=self.clear)
        btn_clear.grid(row=17, column=3, columnspan=2, padx=3, pady=10)

    def recover_passord(self):
        self.master.destroy()
        from Graphic_Interfaces.FormRecoverPassword import instance_form_recover_password
        instance_form_recover_password()

    def logar_user(self):
        nickname = self.nickname.get()
        password = self.password.get()

        if nickname == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite o seu nickname.")
            self.nickname.focus()

        elif len(nickname) < 3:
            tkinter.messagebox.showwarning("Atenção", "Nickname inválido.")
            self.nickname.focus()

        elif password == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite a sua senha. ")
            self.password.focus()

        elif len(password) <= 3:
            tkinter.messagebox.showwarning("Atenção", "Senha inválida.")
            self.password.focus()

        else:
            logar = LoginFuntionalities()
            login = logar.logar(nickname, password)
            self.clear()

            if login['login_ativo'] == "Y":
                self.master.destroy()
                from Graphic_Interfaces.FormMainMenu import instance_form_menu
                instance_form_menu(login['id_login'])

    def create_login(self):
        self.master.destroy()
        from Graphic_Interfaces.FormCreateLogin import instance_form_create_login
        instance_form_create_login()

    def clear(self):
        self.nickname.delete(0, len(self.nickname.get()))
        self.password.delete(0, len(self.password.get()))
        self.nickname.focus()


def instance_form_login():
    form_login = Tk()
    FormLogin(form_login)
    form_login.iconbitmap(r"Images/IconeAgenda.ico")
    form_login.configure(relief="ridge", bg="light gray", border="4")
    form_login.geometry("400x600+520+50")
    form_login.resizable(0, 0)
    form_login.mainloop()
    exit()


# instance_form_login()

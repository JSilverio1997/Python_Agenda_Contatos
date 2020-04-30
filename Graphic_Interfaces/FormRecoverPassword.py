import tkinter.messagebox
from tkinter import *
from Funtionalities.LoginFuntionalities import LoginFuntionalities


class FormRecoverPassword:

    def __init__(self, master):
        self.master = master
        self.master.title("Recuperar senha")
        self.create_comp_form_recover_password(master)

    def create_comp_form_recover_password(self, window):
        lbl_title = Label(text="Recuperar Senha", font="arial, 18", bg="light gray")
        lbl_title.grid(row=1, column=3, pady=10)

        bg_image = tkinter.PhotoImage(file=r"Images/Contact.png")
        canvas_image = Canvas(window, width=200, height=200)
        canvas_image.create_image((0, 0), image=bg_image, anchor=NW)
        canvas_image.image = bg_image
        canvas_image.grid(row=3, column=3, columnspan=1, padx=1, pady=10)

        lbl_nickname = Label(text="Nickname:", font="arial, 14", bg="light gray")
        lbl_nickname.grid(row=6, column=2, pady=2)
        self.lbl_nickname = lbl_nickname

        txt_nickname = Entry(width="25", font="arial,12")
        txt_nickname.grid(row=6, column=3, pady=2)
        txt_nickname.focus()
        self.txt_nickname = txt_nickname

        btn_ok = Button(text="OK", width="10", font="arial,12,bold", command=self.recover_question)
        btn_ok.grid(row=7, column=3, columnspan=2, pady=10)
        self.btn_ok = btn_ok

        btn_clear = Button(text="Limpar", width="10", font="arial", command=self.clear_nickname)
        btn_clear.grid(row=8, column=3, columnspan=2, padx=3, pady=10)
        self.btn_clear = btn_clear

        btn_return = Button(text="Voltar", width="10", font="arial,12,bold", command=self.return_form_login)
        btn_return.grid(row=9, column=3, columnspan=2, pady=10)

        lbl_question = Label(font="arial, 12", bg="light gray")
        lbl_question.grid(row=10, column=3, pady=4)
        self.lbl_question = lbl_question

        lbl_answer = Label(font="arial, 14", bg="light gray")
        lbl_answer.grid(row=14, column=2, pady=4)
        self.lbl_answer = lbl_answer

        txt_answer = Entry(width="25", font="arial, 12")
        self.txt_answer = txt_answer

        btn_answer = Button(text="Resposta", width="10", font="arial,12,bold", command=self.recover_password)
        self.btn_answer = btn_answer

    def clear_nickname(self):
        self.txt_nickname.config(state="normal")
        self.txt_nickname.delete(0, len(self.txt_nickname.get()))
        self.txt_nickname.focus()

    def clear_answer(self):
        self.txt_answer.delete(0, len(self.txt_answer.get()))
        self.txt_answer.focus()

    def recover_question(self):
        if self.txt_nickname.get() == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite um nickname corretamente.")
            self.txt_nickname.focus()
        else:
            login = LoginFuntionalities()
            question = login.return_question(self.txt_nickname.get())
            if question is not None:
                self.txt_nickname.config(state="read")
                self.lbl_question["text"] = question.title()
                self.btn_ok.destroy()
                self.lbl_answer['text'] = "Resposta: "
                self.txt_answer.grid(row=14, column=3, pady=2)
                self.txt_answer.focus_force()
                self.btn_answer.grid(row=15, column=3, columnspan=2, pady=10)
                self.btn_clear['command'] = self.clear_answer
                self.btn_clear.grid(row=16, column=3, columnspan=2, pady=10)

            else:
                tkinter.messagebox.showwarning("Atenção", "O Nickname está incorreto, digite novamente.")
                self.clear_nickname()

    def recover_password(self):
        login = LoginFuntionalities()
        nickname = self.txt_nickname.get()
        answer = self.txt_answer.get()

        if nickname == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite um nickname corretamente.")
            self.txt_nickname.focus()
        elif answer == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite uma respota.")
            self.txt_answer.focus()
        else:
            password = login.recover_password(nickname, answer)
            if password is not None:
                tkinter.messagebox.showinfo("Senha", f"A sua senha é: {password}")
                self.return_form_login()
            else:
                tkinter.messagebox.showwarning("Atenção", "A resposta está incorreta!")
                self.clear_answer()

    def return_form_login(self):
        self.master.destroy()
        from Graphic_Interfaces.FormLogin import instance_form_login
        instance_form_login()


def instance_form_recover_password():
    form_recover_password = Tk()
    FormRecoverPassword(form_recover_password)
    form_recover_password.iconbitmap(r'Images/IconeAgenda.ico')
    form_recover_password.geometry("400x600+520+50")
    form_recover_password.configure(relief="ridge", bg="light gray", border="4")
    form_recover_password.resizable(0, 0)
    form_recover_password.mainloop()
    exit()


# instance_form_recover_password()
